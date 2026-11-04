# Data-vintage robustness: A1 windows on the November 2026 PortWatch pulls (vs frozen July 2026 snapshots)
import pandas as pd, importlib.util, warnings; warnings.filterwarnings('ignore')
spec=importlib.util.spec_from_file_location("eng","src/art41_outcome.py"); eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
R="."  # run from repository root; November pulls expected in art41_snapshots/
PID={"Rotterdam":"port1114","Hamburg":"port446","Antwerp":"port57","Gdansk":"port380","Valencia":"port1348","Piraeus":"port908","TangerMed":"port1265","Mersin":"port735","Singapore":"port1201","Busan":"port1065","PortKlang":"port960","Colombo":"port254","JebelAli":"port744","LA":"port664","NYNJ":"port815","Vancouver":"port1350","Santos":"port1160","Cartagena":"port218","Durban":"port311","Lagos":"port626","Melbourne":"port729","Shanghai":"port1188+port2027"}
jul=pd.read_csv(f"{R}/data/conditions_and_raw_outcomes_v3.csv").set_index("port")
def metrics(wk,w0,w1):
    rc="portcalls_container_yoy_r4"
    win=wk[(wk.week_start>=pd.Timestamp(w0))&wk[rc].notna()].reset_index(drop=True)
    inwin=win[win.week_start<=pd.Timestamp(w1)]
    i=int(inwin[rc].idxmin()); tr=win.loc[i]; after=win.loc[i:].reset_index(drop=True)
    ht=tr[rc]+0.5*(1-tr[rc]); hl=after[after[rc]>=ht]
    hlw=int((hl.iloc[0].week_start-tr.week_start).days//7) if not hl.empty else None
    return round(100*(1-tr[rc]),1), hlw
rows=[]
for p,pid in PID.items():
    r={"port":p}
    for sk,key in (("S1","cov"),("S2","red")):
        df=pd.read_csv(f"art41_snapshots/{pid}_{sk}_raw_20261103.csv"); df["date"]=pd.to_datetime(df["date"])
        sh=eng.SHOCKS[sk]; wk=eng.add_yoy(eng.weekly(df),"portcalls_container",sh["yoy_ref_year"],[])
        d,h=metrics(wk,*sh["window"]); r[f"depth_{key}"]=d; r[f"hl_{key}"]=h
    rows.append(r)
nov=pd.DataFrame(rows).set_index("port")
out=jul[["C1","C2","C3","C4","C5"]].join(nov)
out.reset_index().to_csv(f"{R}/data/window_variants/cond_NOV2026_A1_acute.csv",index=False)
cmp=jul[["depth_cov","hl_cov","depth_red","hl_red"]].join(nov,rsuffix="_nov")
cmp["d_cov"]=cmp.depth_cov_nov-cmp.depth_cov; cmp["d_red"]=cmp.depth_red_nov-cmp.depth_red
print(cmp.round(1).to_string())
print("cells identical (depth&hl):", ((cmp.depth_cov==cmp.depth_cov_nov)&(cmp.hl_cov==cmp.hl_cov_nov)).sum(), ((cmp.depth_red==cmp.depth_red_nov)&(cmp.hl_red==cmp.hl_red_nov)).sum())
