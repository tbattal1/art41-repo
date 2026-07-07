# Results

Computed metrics and weekly series, regenerated from frozen snapshots.

Per run, `art41_outcome.py` writes:
- `{portid}_{shock}_metrics.json` — level (raw/mask/seasonal) + YoY metrics,
  with snapshot SHA and script version stamped in
- `{portid}_{shock}_weekly.csv` — the ISO-weekly series used
- `{portid}_{shock}_log.txt` — run provenance (source, dates, parameters)

Results here are **of record**: they correspond to the committed snapshots and
the locked outcome definition (YoY; see codebook §B). Re-running from the same
snapshot reproduces them byte-for-byte.
