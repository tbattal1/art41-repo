# Data Snapshots

Frozen raw pulls from IMF PortWatch. Each file is a date-stamped snapshot:

```
{portid}_{shock}_raw_{YYYYMMDD}.csv
```

**These files are the reproducibility anchor and MUST be committed to the repo.**
The paper's results are pinned to specific snapshots. To reproduce a published
figure, run `art41_outcome.py` with `--snapshot data/snapshots/<file>`.

To create a snapshot, run the engine once with `--refresh` (or with no snapshot
present); it fetches the live API and writes the dated CSV here.

## Snapshot register

| File | Port | Shock | Pulled (UTC) | SHA-256 (first 12) |
|------|------|-------|--------------|--------------------|
| port1114_S1_raw_20260707.csv | Rotterdam | Ş1 (COVID) | 2026-07-07 | 93af5ebc136e |

*(Extend this table as snapshots are added for the full 22-case run in August.)*
