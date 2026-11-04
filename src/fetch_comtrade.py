"""ART-41 R1 — Comtrade preview pulls for E_R (Q indicator) and E_C partner-weighted robustness.
Reporter list, flows, chapters fixed by exposure_rules_v1 (+ K17b refinement). Each response cached as JSON with SHA-256.
"""
import json, time, hashlib, os, sys, urllib.request, urllib.error, datetime

BASE = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
OUT = "comtrade/raw"; os.makedirs(OUT, exist_ok=True)
REPORTERS = {"NLD":528,"DEU":276,"BEL":56,"POL":616,"ESP":724,"GRC":300,"MAR":504,"TUR":792,
             "SGP":702,"CHN":156,"KOR":410,"MYS":458,"LKA":144,"ARE":784,
             "USA":842,"CAN":124,"BRA":76,"COL":170,"ZAF":710,"NGA":566,"AUS":36}
Q_REPORTERS = ["NLD","DEU","BEL","POL","ESP","GRC","MAR","TUR","SGP","CHN","KOR","MYS","LKA","ARE"]

def pull(reporter, period, cmd, flow):
    fn = f"{OUT}/{reporter}_{period}_{cmd}_{flow}.json"
    if os.path.exists(fn): return fn
    url = (f"{BASE}?reporterCode={REPORTERS[reporter]}&period={period}&cmdCode={cmd}&flowCode={flow}"
           f"&partner2Code=0&customsCode=C00&motCode=0")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=90) as r:
                raw = r.read()
            j = json.loads(raw)
            if j.get("error") or "data" not in j:
                raise RuntimeError(j.get("error"))
            j["_meta"] = {"url": url, "fetched_utc": datetime.datetime.utcnow().isoformat(), "sha256": hashlib.sha256(raw).hexdigest(), "n": len(j["data"])}
            json.dump(j, open(fn, "w"))
            time.sleep(1.5)
            return fn
        except Exception as e:
            wait = 10 * (attempt + 1)
            print(f"retry {reporter} {period} {cmd} {flow}: {e} — sleeping {wait}s", flush=True)
            time.sleep(wait)
    print(f"FAILED {reporter} {period} {cmd} {flow}", flush=True)
    return None

jobs = []
for rep in Q_REPORTERS:
    for flow in ("M", "X"):
        for cmd in ("TOTAL", "25", "26", "27"):
            jobs.append((rep, 2023, cmd, flow))
for rep in REPORTERS:            # partner weights for E_C robustness (pre-shock year)
    for flow in ("M", "X"):
        jobs.append((rep, 2019, "TOTAL", flow))

print(len(jobs), "jobs", flush=True)
for i, jb in enumerate(jobs, 1):
    fn = pull(*jb)
    if i % 10 == 0: print(i, "done", flush=True)
print("ALL DONE", flush=True)
