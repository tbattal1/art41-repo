#!/usr/bin/env python3
"""Graphical abstract (R1). Elsevier spec: >= 1328 x 531 px (w x h), readable at 13 x 5 cm.
Claims follow the revised text (A1 windows, K24): no sufficient configuration for resilience;
fragility patterned differently in the two windows; Durban = lock-in fragility in an unexposed port;
measured exposure neither necessary nor sufficient."""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
plt.rcParams.update({"font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(13, 5), dpi=200); ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 13); ax.set_ylim(0, 5); ax.axis("off")
NAVY, ORG, BLU, GREY = "#1B2A3A", "#B35806", "#2166AC", "#5A6573"

def box(x, y, w, h, fc, ec, lw=1.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.12", fc=fc, ec=ec, lw=lw))

ax.text(0.3, 4.62, "No best model, only best matches: governance configurations and port resilience to two shocks",
        fontsize=14.5, fontweight="bold", color=NAVY, va="center")
ax.text(0.3, 4.22, "22 container ports · 5 governance conditions (C1 autonomy, C2 ownership hybridity, C3 coordination, "
        "C4 compound lock-in, C5 social value) · fsQCA · IMF PortWatch container calls",
        fontsize=10, color=GREY, va="center")

# column 1: design
box(0.3, 0.45, 3.4, 3.35, "#F3F5F7", "#C9CDD2")
ax.text(2.0, 3.5, "Two acute-phase windows", fontsize=11.5, fontweight="bold", color=NAVY, ha="center")
ax.text(0.5, 3.05, "COVID-19 demand collapse\n1 Jan – 30 Sep 2020", fontsize=10, color=NAVY, va="top")
ax.text(0.5, 2.25, "Red Sea rerouting\n19 Nov 2023 – 18 Nov 2024", fontsize=10, color=NAVY, va="top")
ax.text(0.5, 1.45, "Outcome: trough depth × half-life\nof year-on-year container calls,\ncalibrated (0 = fragile, 1 = resilient)",
        fontsize=9, color=GREY, va="top")

# column 2: resilience
box(3.95, 0.45, 2.75, 3.35, "#EEF4FA", BLU)
ax.text(5.32, 3.5, "Resilience", fontsize=11.5, fontweight="bold", color=BLU, ha="center")
ax.text(5.32, 2.65, "No configuration\nis sufficient", fontsize=13, fontweight="bold", color=NAVY, ha="center", va="center")
ax.text(5.32, 1.45, "Resilient ports are governed\nin divergent ways — compatible\nwith, not proof of, equifinality",
        fontsize=9, color=GREY, ha="center", va="top")

# column 3: fragility
box(6.95, 0.45, 5.75, 3.35, "#FBF1E8", ORG)
ax.text(9.82, 3.5, "Fragility: patterned, and differently in each window", fontsize=11.5, fontweight="bold", color=ORG, ha="center")
ax.text(7.15, 3.0, "COVID-19", fontsize=10.5, fontweight="bold", color=NAVY)
ax.text(7.15, 2.68, "~C1 · C2 · ~C3 · ~C4 · ~C5", fontsize=11, family="DejaVu Sans Mono", color=NAVY)
ax.text(7.15, 2.36, "ministry-controlled,\nprivatized ports (4 cases)\ncons. 0.84, PRI 0.73\nthreshold-marginal",
        fontsize=9, color=GREY, va="top")
ax.text(10.15, 3.0, "Red Sea window", fontsize=10.5, fontweight="bold", color=NAVY)
ax.text(10.15, 2.68, "~C1 · ~C2 · ~C3 · C4 · C5", fontsize=11, family="DejaVu Sans Mono", color=NAVY)
ax.text(10.15, 2.36, "compound lock-in in a port\nnot exposed to the rerouting\n(Durban; one case)\ncons. 0.99, PRI 0.96",
        fontsize=9, color=GREY, va="top")
ax.plot([7.15, 12.5], [1.22, 1.22], color="#E3C7AE", lw=0.8)
ax.text(9.82, 0.82, "Measured exposure is neither necessary nor sufficient.\n"
        "The windows differ in context, not in a shock-specific pattern.",
        fontsize=9.5, color=NAVY, ha="center", va="center", style="italic")
ax.text(12.7, 0.12, "~ = absence of a condition;   · = logical AND", fontsize=8, color=GREY, ha="right")
fig.savefig(f"{OUT}/Graphical_Abstract_R1.png", dpi=200); fig.savefig(f"{OUT}/Graphical_Abstract_R1.pdf")
print("ok")
