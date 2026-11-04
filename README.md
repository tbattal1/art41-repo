# No Best Model, Only Best Matches — replication package (revision R1)

Replication package for *No Best Model, Only Best Matches: Governance Configurations, Two Shocks, and the Asymmetry of Port Resilience* (fsQCA; 22 container ports; COVID-19 and Red Sea windows). Manuscript under review at *Research in Transportation Business & Management*, VSI "Port Governance – Reloaded".

**Version 1.2.0 (November 2026)** completes the package that was promised in the submitted manuscript and corrects four coding/analysis items disclosed in the revision (Gdańsk C5, codebook K18; directional expectations for fragility, K19; measurement windows, K22 — the submitted text misstated the windows actually used; the Mersin Red Sea cell, K24 — a pre-existing 2023 decline measured against the 2022 base was reported as Red Sea fragility; see `data/snapshots/README.md` and codebook §B.7–B.9). Version 1.1.0 (July 2026) contained the codebook, four pilot coding sheets, one data snapshot and the analysis script only.

## Contents

```
codebook/
  codebook_v2.9_EN.md          locked coding rules (English edition of v2.6 used for all coding) + revision entries K17–K24
  codebook_v2.6_TR.md          original Turkish working version (July 2026), kept for audit
coding_sheets/
  <port>.md                    22 case coding sheets: every cell with value, source, date, one-line rationale
  exposure_coding.md           remote conditions E_C, E_R: indicators D, Q, Z per port, with sources
  TR_originals/                Turkish working files (July 2026), kept for audit
data/
  conditions_and_raw_outcomes_v4.csv   22 x (C1..C5 as coded, pre tie-break) + trough depth and half-life per shock (A1 windows K22 + K24) — PRIMARY
  conditions_and_raw_outcomes_v3.csv   A1 windows without K24 (audit); v2 = outcome cells of the submitted version (de facto windows)
  window_variants/             outcome tables under alternative windows (J0 de facto, A2-A5, F1-F3), with/without K24, and the Nov 2026 re-pull
  snapshots/july2026/          frozen IMF PortWatch daily series behind Table 4.1 (44 files, SHA-256 register; see snapshots/README.md)
  exposure/                    OxCGRT snapshot note, UN Comtrade raw JSON (154 queries, checksummed), derived tables
src/
  art41_outcome.py             outcome engine v5.3 (snapshot-first; YoY same-ISO-week ratio, 4-week rolling mean; K22 windows, K24 rule)
  outcome_rules.py             shared metric rules (K22/K23/K24) used by july_variants.py and nov_vintage.py
  july_variants.py, grid.py, july_repro.py, nov_vintage.py   window reconstruction and window/vintage sensitivity (K22, K23)
  run_all_snapshots.py         batch runner for 22 ports x 2 shocks (Shanghai = port1188 + port2027)
  e_covid.py, fetch_comtrade.py, compute_Q.py   exposure indicators
  ART41_R1_analysis.R          complete fsQCA analysis: calibration, necessity, sufficiency, robustness, two-step
results/                       outputs of ART41_R1_analysis.R and of the outcome engine (metrics JSON, weekly CSV, logs)
docs/                          design document, pilot decision log, exposure pre-registration (rules fixed before data retrieval)
```

## Reproduce

```bash
# outcome metrics from frozen snapshots (deterministic)
python3 src/art41_outcome.py --portid Rotterdam --shock S1 --snapshot data/snapshots/july2026/Rotterdam_COVID.csv
# full fsQCA analysis (R 4.3.3, QCA 3.25, admisc 0.41)
Rscript src/ART41_R1_analysis.R
# Supplementary S1 tables, figures 1-3 and graphical abstract
Rscript src/export_S1.R && python3 src/build_S1.py
python3 src/make_figure1.py && python3 src/make_figures.py && python3 src/make_graphical_abstract.py results/figures
```

## Notes on provenance

- Governance conditions were coded as of end-2019 by a single coder under the locked codebook; the coding sheets record the source for every cell. The replication of the July 2026 PortWatch pulls in November 2026 is documented in `data/snapshots/README.md`, including any differences caused by PortWatch's retroactive revisions.
- The exposure conditions were added at revision; their rules were fixed and archived (`docs/exposure_rules_v1.md`) before any data were retrieved, and the two subsequent amendments (anchor source; Z definition) are logged with their reasons in the codebook (K17a, K17c).

## Licence

Code: MIT. Data, codebook and coding sheets: CC-BY-4.0.
