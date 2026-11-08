#!/usr/bin/env python3
"""Figure 1 (R1): the study's workflow, from case selection to validation (Section 3).

Pure layout figure (no data). Run from the repository root: python3 src/make_figure_workflow.py
"""
import textwrap, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

REPO = "."
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5})

STEPS = [  # (title, detail, section)
 ("1  Cases", "22 container ports in 7 world regions, selected on size and regional spread before any data were examined", "§3.2"),
 ("2  Governance conditions, end-2019", "C1 regulatory autonomy · C2 ownership hybridity · C3 coordination density · C4 compound lock-in · C5 social-value integration\n"
  "Coded from laws, concession contracts and corporate records under a fixed codebook (v2.9) with a public change log", "§3.3–3.4"),
 ("3  Outcome: recovery from each shock", "IMF PortWatch container vessel calls, frozen snapshots (SHA-256)\n"
  "Two acute-phase windows: 1 Jan–30 Sep 2020 and 19 Nov 2023–18 Nov 2024\nDepth × half-life of the fall = resilience loss; pre-shock level rule", "§3.5, Fig. 3"),
 ("4  Calibration", "Conditions: written anchors for full membership, crossover (0.5) and non-membership\n"
  "Outcome: direct method on resilience loss, 90th / 50th / 10th percentile anchors, each shock separately", "§3.4–3.5"),
 ("5  Fuzzy-set QCA, each shock separately", "Necessity tests (consistency 0.90, relevance of necessity) → truth table (1 case per row, consistency 0.80, PRI 0.70)\n"
  "→ conservative solution (headline) and intermediate solution (Table 2.2 expectations), for resilience and for fragility", "§3.6, §4.2–4.4"),
 ("6  Robustness and validation", "Eleven robustness tests (anchors, tie-break, windows, leave-one-out, data re-pull)\n"
  "Exposure as a remote condition in a two-step analysis (E_C, E_R) · within-case validation of two typical cases and the deviant case", "§4.5–4.6, §5.8"),
]

fig, ax = plt.subplots(figsize=(6.8, 9.6), dpi=300)
ax.set_xlim(0, 10); ax.set_ylim(0, 12.4); ax.axis("off")
x0, w = 0.3, 7.5
gap = 0.3
y = 12.15
centres = []
for title, detail, sec in STEPS:
    lines = []
    for para in detail.split("\n"): lines += textwrap.wrap(para, 68)
    h = 0.55 + 0.235 * len(lines)
    y -= h
    ax.add_patch(FancyBboxPatch((x0, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", linewidth=0.9, edgecolor="0.2", facecolor="0.96", zorder=2))
    ax.text(x0 + 0.18, y + h - 0.17, title, fontsize=9.2, fontweight="bold", va="top", zorder=3)
    ax.text(x0 + 0.18, y + h - 0.47, "\n".join(lines), fontsize=7.4, va="top", linespacing=1.35, zorder=3)
    ax.text(x0 + w - 0.12, y + h - 0.17, sec, fontsize=7.4, va="top", ha="right", color="0.35", zorder=3)
    centres.append((y, y + h))
    y -= gap
for lo, up in zip(centres[1:], centres[:-1]):
    ax.add_patch(FancyArrowPatch((x0 + w / 2, up[0]), (x0 + w / 2, lo[1]), arrowstyle="-|>", mutation_scale=12, linewidth=0.9, color="0.2", shrinkA=0, shrinkB=0, zorder=1))
# side inputs
sx, sw = 8.2, 1.6
def side(label, step_idx, yoff=0.0):
    ya, yb = centres[step_idx]; yc = (ya + yb) / 2 + yoff
    ax.add_patch(FancyBboxPatch((sx, yc - 0.55), sw, 1.1, boxstyle="round,pad=0.02,rounding_size=0.1", linewidth=0.8, edgecolor="0.4", facecolor="white", linestyle="--"))
    ax.text(sx + sw / 2, yc, label, fontsize=6.4, ha="center", va="center", linespacing=1.3)
    ax.add_patch(FancyArrowPatch((sx, yc), (x0 + w, yc), arrowstyle="-|>", mutation_scale=9, linewidth=0.7, color="0.4", shrinkA=0, shrinkB=0))
side("Port Reform\nToolkit\nmodels\n(Table 2.1)", 1, 0.0)
side("Directional\nexpectations\n(Table 2.2)", 4, 0.0)
side("Exposure\ndata: OxCGRT,\nSuez lane\nindex", 5, 0.0)
ax.text(x0, max(0.05, y - 0.1), "Every step is reproducible from the released package (codebook, coding sheets, frozen data, R and Python code).", fontsize=7, color="0.3", va="bottom")
ax.set_ylim(y - 0.55, 12.4)
fig.savefig(f"{REPO}/results/figures/Figure1_R1.png", bbox_inches="tight"); fig.savefig(f"{REPO}/results/figures/Figure1_R1.pdf", bbox_inches="tight")
print("Figure 1 (workflow) written")
