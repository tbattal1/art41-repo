#!/usr/bin/env python3
"""Data-vintage check: A1 windows (K22) with K24 on the November 2026 PortWatch re-pull vs the frozen July 2026 snapshots.
Run from the repository root; the November pulls ({portid}_{S1|S2}_raw_20261103.csv) are expected in art41_snapshots/."""
import pandas as pd, importlib.util, warnings, sys; warnings.filterwarnings('ignore')
spec = importlib.util.spec_from_file_location("eng", "src/art41_outcome.py"); eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
sys.path.insert(0, 'src'); from outcome_rules import metrics
PID = {"Rotterdam":"port1114","Hamburg":"port446","Antwerp":"port57","Gdansk":"port380","Valencia":"port1348","Piraeus":"port908","TangerMed":"port1265","Mersin":"port735","Singapore":"port1201","Busan":"port1065","PortKlang":"port960","Colombo":"port254","JebelAli":"port744","LA":"port664","NYNJ":"port815","Vancouver":"port1350","Santos":"port1160","Cartagena":"port218","Durban":"port311","Lagos":"port626","Melbourne":"port729","Shanghai":"port1188+port2027"}
NOV = "art41_snapshots"; STAMP = "20261103"
jul = pd.read_csv("data/conditions_and_raw_outcomes_v4.csv").set_index("port")
rows = []
for p, pid in PID.items():
    r = {"port": p}
    for sk, key in (("S1", "cov"), ("S2", "red")):
        df = pd.read_csv(f"{NOV}/{pid}_{sk}_raw_{STAMP}.csv"); df["date"] = pd.to_datetime(df["date"])
        sh = eng.SHOCKS[sk]; wk = eng.add_yoy(eng.weekly(df), "portcalls_container", sh["yoy_ref_year"], [])
        d, h, *_ = metrics(wk, *sh["window"]); r[f"depth_{key}"] = d; r[f"hl_{key}"] = h
    rows.append(r)
nov = pd.DataFrame(rows).set_index("port")
jul[["C1", "C2", "C3", "C4", "C5"]].join(nov).reset_index().to_csv("data/window_variants/cond_NOV2026_A1_acute.csv", index=False)
cmp = jul[["depth_cov", "hl_cov", "depth_red", "hl_red"]].join(nov, rsuffix="_nov")
print("cells identical (depth & half-life): COVID", ((cmp.depth_cov == cmp.depth_cov_nov) & (cmp.hl_cov == cmp.hl_cov_nov)).sum(),
      "/22; Red Sea", ((cmp.depth_red == cmp.depth_red_nov) & (cmp.hl_red == cmp.hl_red_nov)).sum(), "/22")
