# Frozen IMF PortWatch snapshots

## july2026/ — the series behind the submitted Table 4.1 (primary data)

44 files `{Port}_{COVID|RedSea}.csv` (columns `date, portcalls, portcalls_container`; daily, 2019-01-01 → 2026-07-03, 2,741 rows each; the COVID and RedSea files of a port are identical copies kept for audit) plus `port1114_S1_raw_20260707.csv`, the only raw engine file surviving from the July 2026 pulls (Rotterdam, 1,000 records — evidence of the ArcGIS `maxRecordCount` truncation that was later fixed in engine v5.1; it is **not** used in any result).

`SHA256_REGISTER.csv` lists the SHA-256 of every file. The SHA-256 (first 12 hex) of each series matches the `snapshot_sha` recorded in the July 2026 result register (`ART41_outcome_results.csv`, 44/44), i.e. these are the exact files from which the submitted outcome metrics were computed.

Shanghai = sum of PortWatch `port1188` (Shanghai) and `port2027` (Yangshan) by date.

## Measurement windows (codebook K22)

The primary outcome metrics in `data/conditions_and_raw_outcomes_v4.csv` are computed on these files with the acute-phase windows COVID 2020-01-01 – 2020-09-30 and Red Sea 2023-11-19 – 2024-11-18 (K22) and the pre-shock level rule K24 (`src/july_variants.py`, variant `A1_acute`; identical results from `src/art41_outcome.py` v5.3 with `--snapshot`). K24 changes two cells: Mersin Red Sea 32.0 %/6 wk → 5.4 %/1 wk (the 2023 decline against the 2022 base pre-dated the shock and reversed during it) and Colombo Red Sea 4.4 %/1 → 0/0. `conditions_and_raw_outcomes_v3.csv` (A1 without K24) is kept for audit.

The submitted version de facto used COVID 2020-02-24 – 2020-10-04 and Red Sea 2023-11-26 – 2024-09-26 (recovered empirically by `src/grid.py`; 44/44 cells reproduced), while the text stated Jan 2020 – Dec 2021 and Oct 2023 – Jun 2025. See codebook §B.7–B.9 for the disclosures and `data/window_variants/` for the outcome tables under each alternative window (J0 de facto, A2 holiday mask, A3/A4 Red Sea start 15 Dec / 1 Dec 2023, A5 six-month window, F1–F3 full windows), each with and without K24 (`_noK24`).

## November 2026 re-pull (data-vintage check)

All 22 ports × 2 shocks were re-pulled from the PortWatch API on 2026-11-03 with engine v5.1 (paginated; files `{portid}_{S1|S2}_raw_20261103.csv`, not stored here because they duplicate the July series). Comparison on all 60,566 overlapping port-days: 3 days differ (Singapore 2024-10-30; Shanghai 2024-01-03 and 2025-02-07 — PortWatch retroactive revisions), none inside a trough or half-life path. Under the A1 windows with K24 the November data reproduce all 44 cells of `conditions_and_raw_outcomes_v4.csv` exactly (`data/window_variants/cond_NOV2026_A1_acute.csv`; `src/nov_vintage.py`). The earlier comparison file `snapshot_rerun_comparison_20261103.csv` was produced with the full stated windows and is kept for audit only; its `_now` columns are not comparable to Table 4.1.

## Known data anomaly (codebook K23)

Colombo, 11 Sep – 29 Oct 2023: all vessel-type series fall simultaneously by ≈ 50 % against the reference year (AIS coverage gap, present in both vintages). It lies outside the A1 Red Sea window; the K23 mask applies only in full-window robustness runs.
