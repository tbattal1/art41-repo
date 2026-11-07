#!/usr/bin/env python3
"""Figures 3 and 4 for ART-41 R1 from results/calibrated_matrix_R1.csv (A1 windows + K24)."""
import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from adjustText import adjust_text

REPO = "."  # run from the repository root after ART41_R1_analysis.R
d = pd.read_csv(f"{REPO}/results/calibrated_matrix_R1.csv", index_col=0)  # memberships from ART41_R1_analysis.R
ST = pd.read_csv(f"{REPO}/results/figures/fig_stats.csv")  # pof() statistics from R, so figure labels match the text
NAMES = {"Rotterdam":"Rotterdam","Hamburg":"Hamburg","Antwerp":"Antwerp","Gdansk":"Gdańsk","Valencia":"Valencia","Piraeus":"Piraeus",
 "TangerMed":"Tanger Med","Mersin":"Mersin","Singapore":"Singapore","Shanghai":"Shanghai","Busan":"Busan","PortKlang":"Port Klang",
 "Colombo":"Colombo","JebelAli":"Jebel Ali","LA":"Los Angeles","NYNJ":"New York/NJ","Vancouver":"Vancouver","Santos":"Santos",
 "Cartagena":"Cartagena","Durban":"Durban","Lagos":"Lagos (Apapa)","Melbourne":"Melbourne"}

def nec(x, y):
    m = np.minimum(x, y); return m.sum()/y.sum(), (1-x).sum()/(1-m).sum(), m.sum()/x.sum()      # inclN, RoN, covN
def suf(x, y):
    m = np.minimum(x, y); m2 = np.minimum.reduce([x, y, 1-y])
    return m.sum()/x.sum(), (m.sum()-m2.sum())/(x.sum()-m2.sum()), m.sum()/y.sum()               # inclS, PRI, covS

d["nC4"] = 1 - d.C4; d["Ycov_n"] = 1 - d.Ycov; d["Yred_n"] = 1 - d.Yred
d["durban_path"] = np.minimum.reduce([1-d.C1, 1-d.C2, 1-d.C3, d.C4, d.C5])
d["hav_path"] = np.minimum.reduce([d.C1, d.C2, d.C3, 1-d.C4, d.C5])

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})

# ---------------- Figure 3 ----------------
fig, axes = plt.subplots(1, 3, figsize=(12, 4.3), dpi=300)
panels = [
 ("nC4", "Ycov", "necessity", "(a) Necessity: ~C4 → resilience, COVID-19", "~C4 (absence of compound lock-in)", "Resilience to the COVID-19 shock", {"Durban": (6, 4), "Piraeus": (6, 4), "Shanghai": (6, -9)}),
 ("nC4", "Yred", "necessity", "(b) Necessity: ~C4 → resilience, Red Sea window", "~C4 (absence of compound lock-in)", "Resilience to the Red Sea-window shock", {"Durban": (6, 4), "Mersin": (6, 2), "Singapore": (6, -9)}),
 ("durban_path", "Yred_n", "sufficiency", "(c) Sufficiency: ~C1·~C2·~C3·C4·C5 → fragility, Red Sea window", "~C1·~C2·~C3·C4·C5 (Durban path)", "Fragility in the Red Sea window (~Y)", {"Durban": (6, 4), "Piraeus": (6, 4), "Vancouver": (8, -4), "Melbourne": (8, -3)}),
]
for ax, (xc, yc, rel, title, xl, yl, lab) in zip(axes, panels):
    x, y = d[xc].values, d[yc].values
    ax.plot([0, 1], [0, 1], color="0.75", lw=0.8, zorder=1)
    ax.axhline(0.5, ls="--", color="0.6", lw=0.7); ax.axvline(0.5, ls="--", color="0.6", lw=0.7)
    ax.scatter(x, y, s=28, facecolor="0.35", edgecolor="black", lw=0.5, zorder=3)
    for p, off in lab.items():
        ax.annotate(NAMES[p], (d.loc[p, xc], d.loc[p, yc]), xytext=off, textcoords="offset points", fontsize=7.5)
    a, b, c = (nec(x, y) if rel == "necessity" else suf(x, y))
    r = ST.iloc[list(axes).index(ax)]; assert abs(r.a - a) < 2e-3 and abs(r.b - b) < 2e-3, (title, a, r.a)
    a, b, c = r.a, r.b, r.c
    sub = (f"Incl. N = {a:.3f}   RoN = {b:.3f}   Cov. N = {c:.3f}" if rel == "necessity" else f"Incl. S = {a:.3f}   PRI = {b:.3f}   Cov. S = {c:.3f}")
    ax.set_title(title, fontsize=8.5, fontweight="bold", loc="left", pad=14)
    ax.text(0.0, 1.015, sub, transform=ax.transAxes, fontsize=7.5, color="0.3", va="bottom")
    ax.set_xlabel(xl, fontsize=8.5); ax.set_ylabel(yl, fontsize=8.5)
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(-0.03, 1.03); ax.set_aspect("equal")
    ax.set_xticks(np.arange(0, 1.01, 0.2)); ax.set_yticks(np.arange(0, 1.01, 0.2))
    ax.tick_params(labelsize=7.5)
    print(title, "->", sub)
fig.tight_layout(w_pad=2.0)
fig.savefig(f"{REPO}/results/figures/Figure3_R1.png", bbox_inches="tight"); fig.savefig(f"{REPO}/results/figures/Figure3_R1.pdf", bbox_inches="tight"); plt.close(fig)

# ---------------- Figure 4 ----------------
fig, ax = plt.subplots(figsize=(7.2, 6.3), dpi=300)
ax.axhline(0.5, ls="--", color="0.5", lw=0.9); ax.axvline(0.5, ls="--", color="0.5", lw=0.9)
ax.grid(True, color="0.92", lw=0.6); ax.set_axisbelow(True)
ax.scatter(d.Ycov, d.Yred, s=60, facecolor="0.25", edgecolor="black", lw=0.6, zorder=3)
MANUAL = {"TangerMed": (1.04, 0.975, "right", "bottom"), "Valencia": (0.80, 0.955, "right", "center"), "Mersin": (0.86, 0.84, "right", "center"), "JebelAli": (1.04, 0.72, "right", "bottom")}
for p, (xx, yy, ha, va) in MANUAL.items():
    ax.annotate(NAMES[p], (d.loc[p, "Ycov"], d.loc[p, "Yred"]), xytext=(xx, yy), textcoords="data", fontsize=8.5, ha=ha, va=va,
                arrowprops=dict(arrowstyle="-", color="0.5", lw=0.5, shrinkA=1, shrinkB=4))
auto = [p for p in d.index if p not in MANUAL]
texts = [ax.text(d.loc[p, "Ycov"], d.loc[p, "Yred"], NAMES[p], fontsize=8.5) for p in auto]
adjust_text(texts, x=d.Ycov.values, y=d.Yred.values, ax=ax, expand_points=(1.4, 1.6), arrowprops=dict(arrowstyle="-", color="0.5", lw=0.5, shrinkA=2, shrinkB=3))
for xx, yy, t, ha, va in [(0.01, 1.04, "Red Sea window only", "left", "top"), (0.99, 1.04, "resilient to both", "right", "top"),
                          (0.01, -0.04, "fragile to both", "left", "bottom"), (0.99, -0.04, "COVID-19 only", "right", "bottom")]:
    ax.text(xx, yy, t, fontsize=9, style="italic", color="0.45", ha=ha, va=va)
ax.set_xlim(-0.06, 1.06); ax.set_ylim(-0.07, 1.07)
ax.set_xlabel("Resilience to the COVID-19 shock (fuzzy-set membership)", fontsize=10)
ax.set_ylabel("Resilience to the Red Sea-window shock (fuzzy-set membership)", fontsize=10)
fig.tight_layout(); fig.savefig(f"{REPO}/results/figures/Figure4_R1.png", bbox_inches="tight"); fig.savefig(f"{REPO}/results/figures/Figure4_R1.pdf", bbox_inches="tight")
print("off-diagonal:", [NAMES[p] for p in d.index if (d.loc[p,"Ycov"]>0.5) != (d.loc[p,"Yred"]>0.5)])
