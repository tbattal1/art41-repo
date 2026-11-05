#!/usr/bin/env python3
"""Figure 1 (R1): calibrated resilience by port, two shock windows, on a world map.
Changes vs. submitted version (R2: labels masked the circles; colour palette not colour-blind safe;
Mersin annotation withdrawn under codebook K24):
  - colour-blind-safe diverging palette (orange = fragile, blue = resilient; ColorBrewer PuOr-like ends),
    plus redundant shape coding (square = membership < 0.5, circle = > 0.5) so the figure reads in greyscale;
  - port numbers sit OUTSIDE the markers with leader lines; NW-Europe and Malacca clusters spread manually;
  - no narrative annotations; window dates in panel titles; legend laid out inside the figure.
Input: results/calibrated_matrix_R1.csv (A1 windows + K24)."""
import warnings; warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
import shapefile
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import sys
REPO = sys.argv[1] if len(sys.argv) > 1 else "."
d = pd.read_csv(f"{REPO}/results/calibrated_matrix_R1.csv", index_col=0)

PORTS = [  # (key, display name, lat, lon, label offset in points (dx, dy))
 ("Rotterdam", "Rotterdam", 51.95, 4.13, (-14, 10)), ("Hamburg", "Hamburg", 53.54, 9.97, (8, 13)),
 ("Antwerp", "Antwerp", 51.27, 4.33, (-15, -9)), ("Gdansk", "Gdańsk", 54.40, 18.67, (12, 9)),
 ("Valencia", "Valencia", 39.44, -0.32, (12, 8)), ("Piraeus", "Piraeus", 37.94, 23.62, (-6, 14)),
 ("TangerMed", "Tanger Med", 35.89, -5.50, (-15, -9)), ("Mersin", "Mersin", 36.79, 34.64, (12, 10)),
 ("Singapore", "Singapore", 1.26, 103.84, (13, -11)), ("Shanghai", "Shanghai", 31.23, 121.85, (-15, -9)),
 ("Busan", "Busan", 35.10, 129.04, (13, 9)), ("PortKlang", "Port Klang", 3.00, 101.39, (-15, 8)),
 ("Colombo", "Colombo", 6.95, 79.85, (-15, -9)), ("JebelAli", "Jebel Ali", 25.01, 55.06, (13, 9)),
 ("LA", "Los Angeles", 33.74, -118.26, (-15, -9)), ("NYNJ", "New York/NJ", 40.67, -74.04, (13, 9)),
 ("Vancouver", "Vancouver", 49.29, -123.11, (-15, 8)), ("Santos", "Santos", -23.96, -46.30, (13, -9)),
 ("Cartagena", "Cartagena", 10.39, -75.53, (-15, 6)), ("Durban", "Durban", -29.87, 31.03, (13, -9)),
 ("Lagos", "Lagos (Apapa)", 6.44, 3.37, (-6, -15)), ("Melbourne", "Melbourne", -37.83, 144.92, (13, -9)),
]
# cartographic displacement for clustered ports: marker drawn at (lat, lon) below, joined to the true location
DISP = {"Rotterdam": (54.6, 0.6), "Antwerp": (49.2, 1.6), "PortKlang": (6.4, 97.6), "Singapore": (-2.2, 106.6)}
# colour-blind-safe diverging map (ends of ColorBrewer PuOr / RdBu family: orange-brown to blue)
CMAP = LinearSegmentedColormap.from_list("frag_res", ["#B35806", "#F1A340", "#F7F7F7", "#67A9CF", "#2166AC"])
NORM = Normalize(0, 1)

# Natural Earth 1:110m countries (public domain), as shipped with geopandas 0.14 (naturalearth_lowres); read with pyshp
NE = sys.argv[2] if len(sys.argv) > 2 else f"{REPO}/data/basemap/naturalearth_lowres.shp"
sf = shapefile.Reader(NE); fields = [f[0] for f in sf.fields[1:]]
POLYS = []
for rec, shp in zip(sf.records(), sf.shapes()):
    if dict(zip(fields, rec)).get("continent") == "Antarctica": continue
    pts = shp.points; parts = list(shp.parts) + [len(pts)]
    for a, b in zip(parts[:-1], parts[1:]): POLYS.append(Polygon(pts[a:b], closed=True))

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(11, 12.2), dpi=300)
axA = fig.add_axes([0.03, 0.555, 0.94, 0.40]); axB = fig.add_axes([0.03, 0.135, 0.94, 0.40])
panels = [(axA, "Ycov", "A   COVID-19 window (1 Jan – 30 Sep 2020): calibrated resilience"),
          (axB, "Yred", "B   Red Sea window (19 Nov 2023 – 18 Nov 2024): calibrated resilience")]
for ax, col, title in panels:
    ax.add_collection(PatchCollection(POLYS, facecolor="#E6E8EB", edgecolor="#C9CDD2", linewidth=0.3, zorder=1)); ax.set_aspect("equal")
    ax.set_xlim(-140, 165); ax.set_ylim(-48, 72); ax.set_axis_off()
    ax.set_title(title, loc="left", fontsize=12.5, fontweight="bold", color="#1B2A3A", pad=6)
    for i, (k, name, lat, lon, off) in enumerate(PORTS, start=1):
        v = float(d.loc[k, col]); mk = "o" if v > 0.5 else "s"
        if k in DISP:
            ax.plot([lon, DISP[k][1]], [lat, DISP[k][0]], color="#5A6573", lw=0.6, zorder=3)
            ax.scatter(lon, lat, s=6, c="#1B2A3A", zorder=3); lat, lon = DISP[k]
        ax.scatter(lon, lat, s=95 if mk == "o" else 80, marker=mk, c=[CMAP(NORM(v))], edgecolor="#1B2A3A", linewidth=0.7, zorder=4)
        ax.annotate(str(i), (lon, lat), xytext=off, textcoords="offset points", fontsize=8.5, fontweight="bold", color="#1B2A3A",
                    ha="center", va="center", zorder=5,
                    arrowprops=dict(arrowstyle="-", color="#5A6573", lw=0.5, shrinkA=1, shrinkB=6))

# colour bar
cax = fig.add_axes([0.30, 0.105, 0.40, 0.012])
sm = plt.cm.ScalarMappable(cmap=CMAP, norm=NORM); cb = fig.colorbar(sm, cax=cax, orientation="horizontal", ticks=[0, 0.5, 1])
cb.ax.tick_params(labelsize=9); cb.outline.set_linewidth(0.5)
cax.set_title("fuzzy-set resilience  (0 = fragile, 1 = resilient);  ■ below 0.5,  ● above 0.5", fontsize=9, pad=4)

# legend: three columns of port numbers, inside the figure
lax = fig.add_axes([0.05, -0.02, 0.90, 0.105]); lax.set_axis_off()
lax.add_patch(plt.Rectangle((0, 0), 1, 1, transform=lax.transAxes, facecolor="#F3F5F7", edgecolor="#C9CDD2", lw=0.6))
cols = [PORTS[0:8], PORTS[8:15], PORTS[15:22]]; start = [1, 9, 16]
for c, (grp, s0) in enumerate(zip(cols, start)):
    for r, p in enumerate(grp):
        lax.text(0.04 + c * 0.33, 0.93 - r * 0.112, f"{s0 + r}. {p[1]}", transform=lax.transAxes, fontsize=8.3, va="top", color="#2B3A4A")
fig.savefig(f"{REPO}/results/figures/Figure1_R1.png", bbox_inches="tight", dpi=300)
fig.savefig(f"{REPO}/results/figures/Figure1_R1.pdf", bbox_inches="tight")
print("ok")
