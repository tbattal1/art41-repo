#!/usr/bin/env python3
"""
ART-41 — outcome metrics under alternative measurement windows (codebook K22) with the
pre-shock-level rule K24 and the optional holiday mask (A2/F2 variants).

Run from the repository root:  python3 src/july_variants.py
Inputs : data/snapshots/july2026/{Port}_{COVID|RedSea}.csv  (frozen PortWatch daily series)
         data/conditions_and_raw_outcomes_v2.csv            (C1..C5 as coded; outcome cells ignored)
Outputs: data/window_variants/cond_JUL_{tag}.csv        K24 applied (primary rule set)
         data/window_variants/cond_JUL_{tag}_noK24.csv  K24 not applied (sensitivity)
         data/window_variants/cond_JUL_{tag}_full.csv   + trough dates, pre-window level, K24 flags
The A1_acute table with K24 is the primary data file (copied to data/conditions_and_raw_outcomes_v4.csv).

Metric definitions (codebook Section B):
  ratio_t   = container calls in ISO week t / same ISO week of the reference year (2019 | 2022), 4-week rolling mean
  trough    = minimum ratio inside the window; depth % = 100 (1 - trough)
  half-life = weeks from the trough to the first week with ratio >= trough + 0.5 (1 - trough)
K24 (pre-shock level): let pre = mean ratio over the 8 weeks before the window. If |pre - 1| > 0.15 and the
  trough falls in the first 4 window weeks, the decline pre-dates the shock; the shock-attributable depth is
  100 (1 - trough/pre) (floored at 0) and the half-life target is trough + 0.5 (pre - trough).
  Not applicable to the COVID window (reference year 2019 = series start, no pre-window ratios).
K23 (holiday mask, variants A2/F2 only): ISO weeks 51-53 and 1 excluded from the trough search.
"""
import pandas as pd, importlib.util, warnings; warnings.filterwarnings('ignore')
spec = importlib.util.spec_from_file_location("eng", "src/art41_outcome.py"); eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
JUL = 'data/snapshots/july2026'; OUT = 'data/window_variants'
cond = pd.read_csv('data/conditions_and_raw_outcomes_v2.csv'); ports = list(cond.port)
VARIANTS = {  # tag: (COVID window, Red Sea window, holiday mask)
 "J0_exact":        (("2020-02-24", "2020-10-04"), ("2023-11-26", "2024-09-26"), False),  # de facto windows of the submitted version
 "A1_acute":        (("2020-01-01", "2020-09-30"), ("2023-11-19", "2024-11-18"), False),  # PRIMARY (K22)
 "A2_acute_mask":   (("2020-01-01", "2020-09-30"), ("2023-11-19", "2024-11-18"), True),
 "A3_acute_Dec":    (("2020-01-01", "2020-09-30"), ("2023-12-15", "2024-12-14"), False),
 "A4_acute_Dec01":  (("2020-01-01", "2020-09-30"), ("2023-12-01", "2024-11-30"), False),
 "A5_acute_6m":     (("2020-01-01", "2020-09-30"), ("2023-11-19", "2024-05-18"), False),
 "F1_full":         (("2020-01-01", "2021-12-31"), ("2023-10-01", "2025-06-30"), False),
 "F2_full_mask":    (("2020-01-01", "2021-12-31"), ("2023-10-01", "2025-06-30"), True),
 "F3_full_Nov19":   (("2020-01-01", "2021-12-31"), ("2023-11-19", "2025-06-30"), False),
}

import sys; sys.path.insert(0, 'src'); from outcome_rules import metrics

def wk_for(port, sk):
    df = pd.read_csv(f"{JUL}/{port}_{sk}.csv"); df['date'] = pd.to_datetime(df['date'])
    sh = eng.SHOCKS['S1' if sk == 'COVID' else 'S2']
    return eng.add_yoy(eng.weekly(df), 'portcalls_container', sh['yoy_ref_year'], [])
WK = {(p, s): wk_for(p, s) for p in ports for s in ('COVID', 'RedSea')}

import os; os.makedirs(OUT, exist_ok=True)
for tag, (w1, w2, mask) in VARIANTS.items():
    for k24 in (True, False):
        out = cond[['port', 'C1', 'C2', 'C3', 'C4', 'C5']].copy(); full = {}
        for key, sk, w in (("cov", "COVID", w1), ("red", "RedSea", w2)):
            res = [metrics(WK[(p, sk)], *w, mask, k24) for p in ports]
            out[f'depth_{key}'] = [r[0] for r in res]; out[f'hl_{key}'] = [r[1] for r in res]
            full[f'trough_{key}'] = [r[2] for r in res]; full[f'pre_{key}'] = [r[3] for r in res]
            full[f'k24_{key}'] = [r[4] for r in res]; full[f'censored_{key}'] = [r[5] for r in res]
        out.to_csv(f"{OUT}/cond_JUL_{tag}{'' if k24 else '_noK24'}.csv", index=False)
        if k24:
            for k, v in full.items(): out[k] = v
            out.to_csv(f"{OUT}/cond_JUL_{tag}_full.csv", index=False)
            fl = out[out.k24_cov | out.k24_red]
            if len(fl): print(f"{tag}: K24 applied to", ", ".join(f"{r.port} ({'COVID' if r.k24_cov else 'Red Sea'}; pre {r.pre_red if r.k24_red else r.pre_cov})" for r in fl.itertuples()))

# the de facto windows without K24 must reproduce the locked July matrix
j0 = pd.read_csv(f"{OUT}/cond_JUL_J0_exact_noK24.csv"); cmp = cond.merge(j0, on='port', suffixes=('_jul', '_j0'))
same = ((cmp.depth_cov_jul == cmp.depth_cov_j0) & (cmp.hl_cov_jul == cmp.hl_cov_j0) & (cmp.depth_red_jul == cmp.depth_red_j0) & (cmp.hl_red_jul == cmp.hl_red_j0))
print("J0 (no K24) vs locked July matrix: identical ports =", same.sum(), "/22")
