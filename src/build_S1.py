#!/usr/bin/env python3
"""Build Supplementary S1 (markdown -> docx via pandoc) from the repository's results.
Run from the repository root after ART41_R1_analysis.R and export_S1.R:  python3 src/build_S1.py OUT.md"""
import pandas as pd, numpy as np, sys, importlib.util, warnings; warnings.filterwarnings("ignore")
OUT = sys.argv[1] if len(sys.argv) > 1 else "results/S1/Supplementary_S1.md"
N = {"Rotterdam":"Rotterdam","Hamburg":"Hamburg","Antwerp":"Antwerp","Gdansk":"Gdańsk","Valencia":"Valencia","Piraeus":"Piraeus",
 "TangerMed":"Tanger Med","Mersin":"Mersin","Singapore":"Singapore","Shanghai":"Shanghai","Busan":"Busan","PortKlang":"Port Klang",
 "Colombo":"Colombo","JebelAli":"Jebel Ali","LA":"Los Angeles","NYNJ":"New York/NJ","Vancouver":"Vancouver","Santos":"Santos",
 "Cartagena":"Cartagena","Durban":"Durban","Lagos":"Lagos (Apapa)","Melbourne":"Melbourne"}
OUTN = {"Ycov":"resilience, COVID-19 window","Yred":"resilience, Red Sea window","Ycov_n":"fragility, COVID-19 window","Yred_n":"fragility, Red Sea window"}
def tilde(x): return str(x).replace("~", "\\~").replace("*", "·")
def names(cs):
    if not isinstance(cs, str): return ""
    return ", ".join(N.get(c.strip(), c.strip()) for c in cs.split(","))
def md(df, floatfmt=3):
    df = df.copy()
    for c in df.columns:
        if df[c].dtype.kind == "f": df[c] = df[c].map(lambda v: "" if pd.isna(v) else f"{v:.{floatfmt}f}")
    head = "| " + " | ".join(map(str, df.columns)) + " |\n|" + "---|" * len(df.columns) + "\n"
    return head + "".join("| " + " | ".join(map(str, r)) + " |\n" for r in df.values)
L = []; A = L.append
A("---\ntitle: \"Supplementary Material S1 — Analysis details, robustness and outcome measurement\"\n"
  "subtitle: \"No Best Model, Only Best Matches: Governance Configurations, Two Shocks, and the Asymmetry of Port Resilience\"\n---\n")
A("All tables are generated from the replication package (codebook v2.9; `data/conditions_and_raw_outcomes_v4.csv`; scripts `src/ART41_R1_analysis.R`, "
  "`src/export_S1.R`, `src/july_variants.py`, `src/build_S1.py`). Notation: \\~X denotes the absence of condition X and · denotes logical AND. "
  "Thresholds throughout: raw consistency ≥ 0.80, PRI ≥ 0.70, frequency ≥ 1; twelve condition cells at exactly 0.50 recoded to 0.501. "
  "Software: R 4.3.3, QCA 3.25, admisc 0.41; Python 3 (pandas).\n")

# S1.1 raw metrics
f = pd.read_csv("data/window_variants/cond_JUL_A1_acute_full.csv").set_index("port")
t = pd.DataFrame({"Port": [N[p] for p in f.index],
  "COVID depth %": [("no decline" if v < 0 else f"{v:.1f}") for v in f.depth_cov], "COVID half-life (wk)": f.hl_cov.values,
  "COVID trough": [t if d >= 0 else "—" for t, d in zip(f.trough_cov, f.depth_cov)],
  "Red Sea depth %": [("no decline" if v < 0 else f"{v:.1f}") + (" ᵃ" if k else "") for v, k in zip(f.depth_red, f.k24_red)],
  "Red Sea half-life (wk)": f.hl_red.values, "Red Sea trough": [t if d >= 0 else "—" for t, d in zip(f.trough_red, f.depth_red)],
  "Pre-window ratio (Red Sea)": f.pre_red.map(lambda v: f"{v:.2f}").values})
A("# S1.1 Raw outcome metrics\n\nContainer vessel calls, year-over-year ratio to the same ISO week of the reference year (2019; 2022), four-week rolling mean. "
  "Windows: 1 Jan–30 Sep 2020 and 19 Nov 2023–18 Nov 2024 (codebook K22). Trough = Monday of the ISO week.\n\n" + md(t) +
  "\n*ᵃ Pre-shock level rule (K24) applied; uncorrected values: Mersin 32.0 % / 6 wk; Colombo 4.4 % / 1 wk. Negative depths (no decline) enter the loss score as zero. "
  "Durban's pre-window ratio (2.74) reflects the October 2022 Transnet strike in the reference-year denominator; the rule does not apply because its trough falls in window week 7.*\n")
an = pd.DataFrame({"Outcome": ["Loss, COVID-19", "Loss, Red Sea"]})
lc = (f.depth_cov.clip(lower=0) * f.hl_cov); lr = (f.depth_red.clip(lower=0) * f.hl_red)
an["P90 (full non-membership)"] = [lc.quantile(.9), lr.quantile(.9)]; an["P50 (crossover)"] = [lc.quantile(.5), lr.quantile(.5)]; an["P10 (full membership)"] = [lc.quantile(.1), lr.quantile(.1)]
A("**Calibration anchors.** Resilience-loss score = max(0, depth) × half-life; resilience calibrated by the direct method with descending anchors.\n\n" + md(an, 2))
cm = pd.read_csv("results/calibrated_matrix_R1.csv", index_col=0)
A("\n**Calibrated memberships (after tie-break).**\n\n" + md(pd.DataFrame({"Port": [N[p] for p in cm.index], **{c: cm[c].values for c in ["C1","C2","C3","C4","C5","Ycov","Yred","Ycov_B","Yred_B","E_C","E_R"]}})))

# S1.2 truth tables
A("\n# S1.2 Truth tables\n\nObserved rows only (twelve of thirty-two logically possible configurations; diversity ratio 0.375). OUT = 1 marks rows meeting both thresholds.\n")
for o in ["Ycov", "Yred", "Ycov_n", "Yred_n"]:
    tt = pd.read_csv(f"results/S1/truth_table_{o}.csv"); tt["cases"] = tt.cases.map(names)
    tt = tt.rename(columns={"row": "Row", "incl": "Cons.", "cases": "Cases"})
    A(f"\n**Table S1.2-{['Ycov','Yred','Ycov_n','Yred_n'].index(o)+1}. Outcome: {OUTN[o]}.**\n\n" + md(tt))

# S1.3 solutions
s = pd.read_csv("results/S1/solutions.csv")
A("\n# S1.3 Solutions: conservative, parsimonious and intermediate\n\nIntermediate solutions use the directional expectations of Table 4.x "
  "(resilience: C1, C2, C3, C5 present, C4 absent; fragility: the complements, codebook K19). Labels C1P*/M* identify alternative models where minimisation is ambiguous.\n")
for o in ["Ycov", "Yred", "Ycov_n", "Yred_n"]:
    x = s[s.outcome == o].copy(); x["term"] = x.term.map(tilde); x["cases"] = x.cases.map(names)
    x = x[["type", "model", "term", "inclS", "PRI", "covS", "cases"]].rename(columns={"type":"Solution","model":"Model","term":"Term","inclS":"Cons.","covS":"Raw cov.","cases":"Cases (membership > 0.5)"})
    A(f"\n**{OUTN[o].capitalize()}.**\n\n" + md(x))

# S1.4 necessity
ns = pd.read_csv("results/S1/necessity_single.csv"); ns["condition"] = ns.condition.map(tilde)
w = ns.pivot(index="condition", columns="outcome", values="inclN")[["Ycov","Yred","Ycov_n","Yred_n"]]
r = ns.pivot(index="condition", columns="outcome", values="RoN")[["Ycov","Yred","Ycov_n","Yred_n"]]
tab = pd.DataFrame({"Condition": w.index})
for o in ["Ycov","Yred","Ycov_n","Yred_n"]: tab[f"{OUTN[o]} (inclN / RoN)"] = [f"{a:.3f} / {b:.3f}" for a, b in zip(w[o], r[o])]
A("\n# S1.4 Necessity\n\n**Single conditions.** No condition reaches 0.90; inclusion ≥ 0.80 with low RoN reflects skewed memberships (C2 > 0.5 in 77 % of cases, \\~C4 in 86 %).\n\n" + md(tab))
sup = pd.read_csv("results/S1/necessity_supersubset.csv"); sup["expression"] = sup.expression.map(lambda v: tilde(v).replace("+", " + "))
A("\n**Disjunctions with inclN ≥ 0.85 and coverage ≥ 0.50 (superSubset).**\n\n" + md(sup.assign(outcome=sup.outcome.map(OUTN)).rename(columns={"outcome":"Outcome","expression":"Expression"})))

# S1.5 robustness
rob = pd.read_csv("results/robustness_table.csv")
rob = rob.rename(columns={"perturbation":"Perturbation","covid_path":"Pandemic 4-case path","covid_path2":"Pandemic Shanghai–Singapore term","covid_solution":"Pandemic solution",
                          "redsea_path":"Red Sea Durban path","redsea_path2":"Red Sea Hamburg–Antwerp–Vancouver term","redsea_solution":"Red Sea solution"})
for c in ["Pandemic solution", "Red Sea solution"]: rob[c] = rob[c].map(lambda v: tilde(v).replace("+", " + "))
A("\n# S1.5 Robustness (full table)\n\nEach cell: consistency / PRI / raw coverage of the term, recomputed with the outcome recalibrated under the perturbation; solution = conservative minimisation.\n\n" + md(rob))
loo = pd.read_csv("results/leave_one_out.csv"); loo["dropped"] = loo.dropped.map(N)
A("\n**Leave-one-out (outcome recalibrated on 21 cases).**\n\n" + md(loo.rename(columns={"dropped":"Case removed","covid_path":"Pandemic 4-case path","covid_path2":"Pandemic Shanghai–Singapore",
  "redsea_path":"Red Sea Durban path","redsea_path2":"Red Sea Hamburg–Antwerp–Vancouver"})))

# S1.6 window reconstruction
v2 = pd.read_csv("data/conditions_and_raw_outcomes_v2.csv").set_index("port"); v3 = pd.read_csv("data/conditions_and_raw_outcomes_v3.csv").set_index("port")
rows = []
for tag, lab in [("F1_full_noK24", "Stated in the submitted text (1 Jan 2020–31 Dec 2021; 1 Oct 2023–30 Jun 2025)"), ("J0_exact_noK24", "De facto, recovered (24 Feb–4 Oct 2020; 26 Nov 2023–26 Sep 2024)"), ("A1_acute_noK24", "Revision, acute phase (1 Jan–30 Sep 2020; 19 Nov 2023–18 Nov 2024)")]:
    g = pd.read_csv(f"data/window_variants/cond_JUL_{tag}.csv").set_index("port")
    rows.append([lab, f"{((g.depth_cov==v2.depth_cov)&(g.hl_cov==v2.hl_cov)).sum()} / 22", f"{((g.depth_red==v2.depth_red)&(g.hl_red==v2.hl_red)).sum()} / 22"])
A("\n# S1.6 Measurement windows: reconstruction and changed cells\n\nThe frozen July 2026 snapshots (44 series; SHA-256 identical to the July result register) were re-run under alternative windows. "
  "Only the de facto windows reproduce the submitted Table 4.1; they were recovered by a grid search over window bounds (`src/grid.py`).\n\n"
  + md(pd.DataFrame(rows, columns=["Windows", "COVID cells reproducing submitted Table 4.1", "Red Sea cells reproducing submitted Table 4.1"])))
ch = []
for p in v2.index:
    for sh, dc, hc in (("COVID-19", "depth_cov", "hl_cov"), ("Red Sea", "depth_red", "hl_red")):
        if (v2.loc[p, dc], v2.loc[p, hc]) != (v3.loc[p, dc], v3.loc[p, hc]):
            v4 = f.loc[p]
            ch.append([N[p], sh, f"{v2.loc[p, dc]:.1f} / {int(v2.loc[p, hc])}", f"{v3.loc[p, dc]:.1f} / {int(v3.loc[p, hc])}", f"{v4[dc]:.1f} / {int(v4[hc])}"])
A(f"\n**Port–shock cells that change ({len(ch)}).** depth % / half-life (weeks).\n\n" + md(pd.DataFrame(ch, columns=["Port", "Shock", "Submitted (de facto windows)", "Acute windows", "Acute windows + K24"])))

# S1.7 pre-shock rule
pre = pd.DataFrame({"Port": [N[p] for p in f.index], "Pre-window ratio (8 wk)": f.pre_red.map(lambda v: f"{v:.3f}").values,
  "|pre − 1| > 0.15": ["yes" if abs(v - 1) > 0.15 else "" for v in f.pre_red], "Trough week in window": [ (pd.Timestamp(t) - pd.Timestamp("2023-11-19")).days // 7 for t in f.trough_red],
  "K24 applied": ["yes" if k else "" for k in f.k24_red]})
A("\n# S1.7 Pre-shock level rule (K24)\n\nRule: if the mean ratio over the eight weeks before the window departs from unity by more than 0.15 **and** the trough falls in window weeks 0–3, "
  "depth and half-life are measured against the pre-window level. Red Sea window shown; the rule cannot be evaluated for the COVID window (no pre-window ratios for the 2019 base).\n\n" + md(pre))
spec = importlib.util.spec_from_file_location("eng", "src/art41_outcome.py"); eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
df = pd.read_csv("data/snapshots/july2026/Mersin_RedSea.csv"); df["date"] = pd.to_datetime(df["date"])
wk = eng.add_yoy(eng.weekly(df), "portcalls_container", 2022, [])
wk = wk[(wk.week_start >= "2023-09-04") & (wk.week_start <= "2024-03-11")]
A("\n**Mersin, weekly container calls and ratio to the same ISO week of 2022 (September 2023 – March 2024).** The window opens on 19 November 2023.\n\n" +
  md(pd.DataFrame({"Week (Monday)": wk.week_start.dt.date.astype(str).values, "Container calls": wk.portcalls_container.astype(int).values,
                   "Ratio to 2022": wk.portcalls_container_yoy.values, "4-week rolling mean": wk.portcalls_container_yoy_r4.values})))
q = df.assign(q=df.date.dt.to_period("Q")).groupby("q").portcalls_container.mean().loc["2022Q1":"2024Q4"]
A("\n**Mersin, mean daily container calls by quarter.**\n\n" + md(pd.DataFrame({"Quarter": q.index.astype(str), "Mean daily container calls": q.values}), 1))

# S1.8 two-step
ctx = pd.read_csv("results/two_step_contexts.csv"); ctx["port"] = ctx.port.map(N)
A("\n# S1.8 Exposure (two-step) contexts\n\nE_C: OxCGRT stringency, 2020 mean, calibrated on world-distribution anchors (75.67 / 60.49 / 41.48). E_R: rule-based lane-dependence and partner-trade index (codebook §C). "
  "Fragility = 1 − calibrated resilience.\n\n" + md(ctx.rename(columns={"port":"Port","frag_covid":"Fragility, COVID","frag_redsea":"Fragility, Red Sea","ctx_C":"Stringency context","ctx_R":"Rerouting context"}), 2))
A("\n*Step 1: E_C → \\~Y consistency 0.617, PRI 0.455; necessity 0.762, RoN 0.588. E_R → \\~Y consistency 0.672, PRI 0.497; necessity 0.563, RoN 0.808. "
  "Six-condition conservative solution for Red Sea-window fragility: \\~C1·\\~C2·\\~C3·C4·C5·\\~E_R. Within-context minimisations are not reported (case-to-condition benchmark; codebook K17d). "
  "New York–New Jersey E_R at 0.70 instead of 0.40: E_R → \\~Y 0.660 / 0.480; no other change.*\n")

# S1.9 / S1.10
A("\n# S1.9 Calibration B (additive composite)\n\nResilience B = 0.5 (1 − normalised depth) + 0.5 (1 − normalised half-life), calibrated at the 10th / 50th / 90th percentiles. "
  "Results are in the \"calibration B (additive)\" row of S1.5: the Durban path holds (0.933 / 0.717 / 0.202); the pandemic four-case path falls below PRI (0.828 / 0.691 / 0.602); "
  "the Hamburg–Antwerp–Vancouver term does not survive (0.779 / 0.662). The additive composite lets a deep but short trough offset a shallow but long one, which is why the "
  "product (resilience-triangle area) is the primary definition.\n")
A("\n# S1.10 Data vintage\n\nAll 22 ports × 2 shocks were re-pulled from the PortWatch API on 3 November 2026 (engine v5.1, paginated). Of 60,566 overlapping port-days, three differ "
  "(Singapore 30 Oct 2024; Shanghai 3 Jan 2024 and 7 Feb 2025), none on a trough or half-life path. Under the acute windows with K24 the November data reproduce all 44 outcome cells "
  "(`data/window_variants/cond_NOV2026_A1_acute.csv`).\n")
open(OUT, "w").write("\n".join(L)); print("written", OUT)
