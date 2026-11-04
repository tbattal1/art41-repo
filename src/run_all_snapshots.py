import subprocess, json, glob, os, pandas as pd, sys, datetime
ports = {"Rotterdam":"port1114","Hamburg":"port446","Antwerp":"port57","Gdansk":"port380","Valencia":"port1348","Piraeus":"port908",
"TangerMed":"port1265","Mersin":"port735","Singapore":"port1201","Busan":"port1065","PortKlang":"port960","Colombo":"port254",
"JebelAli":"port744","LA":"port664","NYNJ":"port815","Vancouver":"port1350","Santos":"port1160","Cartagena":"port218","Durban":"port311",
"Lagos":"port626","Melbourne":"port729"}
def run(pid, name, shock, snapshot=None):
    if snapshot is None and glob.glob(f"art41_snapshots/{pid}_{shock}_raw_*.csv"):
        print(name, shock, "exists — skip", flush=True); return
    cmd = ["python3","art41_outcome.py","--portid",pid,"--portname",name,"--shock",shock,"--outdir","art41_out"]
    cmd += (["--snapshot",snapshot] if snapshot else ["--refresh"])
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    print(name, shock, "rc", r.returncode, (r.stderr or "")[-200:].replace("\n"," "), flush=True)
for name,pid in ports.items():
    for shock in ("S1","S2"): run(pid,name,shock)
# Shanghai composite: pull both, sum per date, run from combined snapshot
for shock in ("S1","S2"):
    for pid in ("port1188","port2027"): run(pid,"Shanghai_"+pid,shock)
    import time; time.sleep(5)
    a = sorted(glob.glob(f"art41_snapshots/port1188_{shock}_raw_*.csv"))[-1]; b = sorted(glob.glob(f"art41_snapshots/port2027_{shock}_raw_*.csv"))[-1]
    da, db = pd.read_csv(a), pd.read_csv(b)
    cols=[c for c in ["portcalls","portcalls_container","portcalls_cargo","portcalls_tanker"] if c in da.columns and c in db.columns]
    m = da[["date"]+cols].merge(db[["date"]+cols], on="date", how="outer", suffixes=("_a","_b")).fillna(0)
    out = pd.DataFrame({"date": m["date"], "portid": "port1188+port2027"})
    for c in cols: out[c] = m[c+"_a"] + m[c+"_b"]
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    snap = f"art41_snapshots/port1188+port2027_{shock}_raw_{stamp}.csv"; out.sort_values("date").to_csv(snap, index=False)
    run("port1188+port2027","Shanghai",shock,snapshot=snap)
print("DONE", flush=True)
