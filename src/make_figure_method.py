#!/usr/bin/env python3
"""Figure 3 (R1): how the outcome is measured (Section 3.5).

Two worked examples from the frozen July 2026 PortWatch snapshots:
  (a) Rotterdam, COVID-19 window  - the standard measurement (depth, half-life, resilience triangle);
  (b) Mersin, Red Sea window      - the pre-shock level rule (codebook K24).
Numbers printed on the panels come from outcome_rules.metrics(), the same function used for the outcome table.
Run from the repository root: python3 src/make_figure_method.py
"""
import importlib.util, sys, pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.dates import date2num

REPO = "."; sys.path.insert(0, f"{REPO}/src")
from outcome_rules import metrics, RC, PRE_WEEKS
spec = importlib.util.spec_from_file_location("eng", f"{REPO}/src/art41_outcome.py"); eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)

def wk_for(port, sk):
    df = pd.read_csv(f"{REPO}/data/snapshots/july2026/{port}_{sk}.csv"); df["date"] = pd.to_datetime(df["date"])
    sh = eng.SHOCKS["S1" if sk == "COVID" else "S2"]
    return eng.add_yoy(eng.weekly(df), "portcalls_container", sh["yoy_ref_year"], [])

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
GREY, DARK, LIGHT = "0.45", "0.15", "0.88"

def panel(ax, port, sk, w0, w1, show_from, show_to, title, k24_note, hl_dy=0.0, lp_dy=0.018, dp_dx=4, crowded=False):
    wk = wk_for(port, sk)
    depth, hl, trough, pre, flag, cens = metrics(wk, w0, w1)
    w0, w1 = pd.Timestamp(w0), pd.Timestamp(w1)
    s = wk[(wk.week_start >= show_from) & (wk.week_start <= show_to) & wk[RC].notna()]
    ax.plot(s.week_start, s[RC], color=DARK, lw=1.4, zorder=3)
    ax.axvspan(w0, w1, color=LIGHT, zorder=0)                                  # measurement window
    ax.axhline(1.0, color=GREY, lw=0.8, ls="-")                                # reference level
    tr = s[s.week_start == pd.Timestamp(trough)].iloc[0]
    level = pre if flag else 1.0                                                # level from which depth is measured
    t_hl = tr.week_start + pd.Timedelta(weeks=hl)
    # resilience triangle (depth x half-life)
    ax.add_patch(Polygon([[date2num(tr.week_start), level], [date2num(tr.week_start), tr[RC]], [date2num(t_hl), level]], closed=True, facecolor="0.70", edgecolor="none", alpha=0.6, zorder=2))
    ax.plot([tr.week_start], [tr[RC]], "o", ms=5, color="black", zorder=4)
    # depth arrow
    ax.annotate("", xy=(tr.week_start, tr[RC]), xytext=(tr.week_start, level), arrowprops=dict(arrowstyle="<->", color="black", lw=0.9))
    if crowded:
        pass  # depth is written with the low-point label below
    else:
        ax.text(tr.week_start - pd.Timedelta(days=dp_dx), (level + tr[RC]) / 2, f"depth\n{depth:.1f}%", ha="right", va="center", fontsize=8)
    # half-life
    target = tr[RC] + 0.5 * (level - tr[RC])
    ax.hlines(target, tr.week_start, t_hl, color="black", lw=0.8, ls=":")
    ax.annotate("", xy=(t_hl, target), xytext=(tr.week_start, target), arrowprops=dict(arrowstyle="->", color="black", lw=0.9))
    hl_lab = f"half-life\n{hl} week{'s' if hl != 1 else ''}"
    if hl_dy:  # crowded panel: label with a leader line
        ax.annotate(hl_lab, xy=(t_hl, target), xytext=(t_hl + pd.Timedelta(days=28), target + hl_dy), fontsize=8, va="center",
                    arrowprops=dict(arrowstyle="-", color="0.5", lw=0.6))
    else:
        ax.text(t_hl + pd.Timedelta(days=5), target, hl_lab, va="center", fontsize=8)
    if crowded:
        ax.text(tr.week_start + pd.Timedelta(days=10), tr[RC] - lp_dy, f"low point {tr.week_start.date():%d %b %Y}\ndepth {depth:.1f}% below the pre-window level", ha="left", va="top", fontsize=7.5)
    else:
        ax.text(tr.week_start, tr[RC] - lp_dy, f"low point\n{tr.week_start.date():%d %b %Y}", ha="center", va="top", fontsize=7.5)
    if flag:  # pre-shock level rule: show the eight pre-window weeks and the level they define
        ax.axvspan(w0 - pd.Timedelta(weeks=PRE_WEEKS), w0, facecolor="none", edgecolor=GREY, hatch="///", lw=0, zorder=0)
        ax.axhline(pre, color="black", lw=0.9, ls="--")
        ax.text(show_to - pd.Timedelta(days=3), pre + 0.012, f"mean level in the eight weeks before the window = {pre:.2f}", fontsize=7.5, va="bottom", ha="right")
        ax.text(show_from + pd.Timedelta(days=3), 1.0 + 0.012, "reference-year level = 1.00", fontsize=7.5, va="bottom", color=GREY)
    else:
        ax.text(show_from + pd.Timedelta(days=3), 1.0 + 0.008, "reference-year level = 1.00", fontsize=7.5, va="bottom", color=GREY)
    ax.set_title(title, loc="left", fontsize=9.5)
    ax.set_ylabel("Container vessel calls, ratio to the same week of the reference year")
    ax.set_xlim(show_from, show_to)
    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=1)); ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b\n%Y"))
    for sp in ("top", "right"): ax.spines[sp].set_visible(False)
    ax.text(0.99, 0.03, f"resilience loss = depth × half-life = {depth * hl:.0f}{k24_note}", transform=ax.transAxes, ha="right", va="bottom", fontsize=8,
            bbox=dict(facecolor="white", edgecolor="0.7", pad=3))
    return depth, hl, pre, flag

fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), dpi=300)
a = panel(axes[0], "Rotterdam", "COVID", "2020-01-01", "2020-09-30", pd.Timestamp("2020-01-20"), pd.Timestamp("2020-10-19"),
          "(a) Standard measurement\nRotterdam, COVID-19 window (1 Jan–30 Sep 2020; reference year 2019)", "")
# what the Mersin cell would have been without the rule
wk_m = wk_for("Mersin", "RedSea"); d0, h0, *_ = metrics(wk_m, "2023-11-19", "2024-11-18", k24=False)
b = panel(axes[1], "Mersin", "RedSea", "2023-11-19", "2024-11-18", pd.Timestamp("2023-09-04"), pd.Timestamp("2024-04-29"),
          "(b) Pre-shock level rule\nMersin, Red Sea window (19 Nov 2023–18 Nov 2024; reference year 2022)",
          f"\nwithout the rule: depth {d0:.1f}%, half-life {h0} weeks, loss {d0 * h0:.0f}", hl_dy=0.10, lp_dy=0.012, dp_dx=5, crowded=True)
axes[0].set_ylim(0.80, 1.10); axes[1].set_ylim(0.55, 1.12)
axes[1].set_ylabel("")
fig.tight_layout()
fig.savefig(f"{REPO}/results/figures/Figure3_R1.png", bbox_inches="tight"); fig.savefig(f"{REPO}/results/figures/Figure3_R1.pdf", bbox_inches="tight")
print("Rotterdam COVID:", a, "| Mersin Red Sea:", b, "| Mersin without K24:", d0, h0)
