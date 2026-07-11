# Port Governance Configurations and Measured Shock Recovery

Replication package for the study of port governance configurations and measured
shock recovery across the global port system (fsQCA), targeting *Research in
Transportation Business & Management*, VSI **"Port Governance – Reloaded."**

**Working title:** *No Best Model, Only Best Matches: Governance Configurations and
Measured Shock Recovery Across the Global Port System*

---

## What this repository contains

This is a **reproducibility package**. Every governance condition is coded with a
documented source; every outcome metric is computed from a **frozen data snapshot**
so that results do not drift when the upstream API is revised.

```
art41-repo/
├── README.md                  ← this file
├── LICENSE                    ← CC-BY-4.0 (docs/data) + MIT (code)
├── requirements.txt           ← Python dependencies
├── src/
│   └── art41_outcome.py       ← outcome computation engine (v5)
├── data/
│   └── snapshots/             ← frozen raw PortWatch pulls (*_raw_YYYYMMDD.csv)
├── codebook/
│   └── codebook_v2.1.md       ← locked coding rules + change log
├── coding_sheets/             ← per-case condition coding with sources
│   ├── pilot_rotterdam.md
│   ├── pilot_mersin.md
│   ├── pilot_durban.md
│   ├── pilot_melbourne.md
│   └── verification/          ← evidence addenda
├── results/                   ← computed metrics (JSON) + weekly series (CSV)
└── docs/
    ├── design_v2.md           ← research design
    ├── pilot_consolidated.md  ← pilot matrix + decision log
    └── outcome_pilot_note.md  ← Ş1 outcome decision record
```

## Reproducing the outcome metrics

Requirements: Python 3.9+ and the packages in `requirements.txt`.

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Run from a frozen snapshot (deterministic — recommended for replication):**

```bash
python src/art41_outcome.py --portid port1114 --shock S1 \
    --snapshot data/snapshots/port1114_S1_raw_20260707.csv
```

This reads only the frozen CSV, never the live API, so it reproduces the exact
figures in the paper. Each run writes `results/{portid}_{shock}_metrics.json`
(with the snapshot's SHA-256 stamp), a weekly series CSV, and a run log.

**Refresh from the live API (creates a NEW dated snapshot):**

```bash
python src/art41_outcome.py --portid port1114 --portname Rotterdam --shock S1 --refresh
```

> ⚠️ **Why snapshots matter.** IMF PortWatch revises historical data (backfill).
> The same command run days apart can yield different figures. The paper's results
> are pinned to the committed snapshots in `data/snapshots/`. To reproduce the
> published numbers, always pass `--snapshot`.

## Outcome definition (locked)

The recovery outcome **Y** is the **year-over-year (YoY) same-ISO-week ratio**
(4-week rolling mean), which removes calendar seasonality. Reference years:
Ş1 (COVID) → 2019; Ş2 (Red Sea) → 2022. A level-based definition is reported in
the robustness appendix as a definition-sensitivity check. See
`codebook/codebook_v2.1.md` §B and `docs/outcome_pilot_note.md` for the decision
record (four definitions were tested on real Rotterdam data; only YoY located the
actual COVID trough).

## Data source & attribution

Raw vessel-call data: **IMF PortWatch** (portwatch.imf.org), an open dataset.
Snapshots in `data/snapshots/` are date-stamped pulls. Governance coding draws on
primary legal texts, port authority reports, and peer-reviewed literature — each
cited in the coding sheets.
## Requirements

**Python** ≥ 3.8 (see `requirements.txt`) — outcome calibration and PortWatch snapshot freezing (`src/art41_outcome.py`)
**R** 4.3.3 with `QCA` (3.25) and `SetMethods` — configurational analysis (`src/ART41_fsqca.R`)

## Citation

Battal, T. (2026). *No Best Model, Only Best Matches: Governance Configurations and
Measured Shock Recovery Across the Global Port System.* [Under preparation.]

## License

Code: MIT. Documentation, codebook, and coding sheets: CC-BY-4.0. See `LICENSE`.
