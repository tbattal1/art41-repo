import pandas as pd, numpy as np, importlib.util, warnings; warnings.filterwarnings('ignore')
spec=importlib.util.spec_from_file_location("eng","src/art41_outcome.py"); eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
JUL='data/snapshots/july2026'  # run from repository root
cond=pd.read_csv('data/conditions_and_raw_outcomes_v2.csv')
ports=list(cond.port)
VARIANTS={
 # tag: (S1 window, S2 window, mask)
 "J0_exact":     (("2020-02-24","2020-10-04"),("2023-11-26","2024-09-26"),False),
 "J1_exact_fullend":(("2020-02-24","2021-12-31"),("2023-11-26","2025-06-30"),False),
 "A1_acute":     (("2020-01-01","2020-09-30"),("2023-11-19","2024-11-18"),False),
 "A2_acute_mask":(("2020-01-01","2020-09-30"),("2023-11-19","2024-11-18"),True),
 "A3_acute_Dec": (("2020-01-01","2020-09-30"),("2023-12-15","2024-12-14"),False),
 "F1_full":      (("2020-01-01","2021-12-31"),("2023-10-01","2025-06-30"),False),
 "F2_full_mask": (("2020-01-01","2021-12-31"),("2023-10-01","2025-06-30"),True),
 "F3_full_Nov19":(("2020-01-01","2021-12-31"),("2023-11-19","2025-06-30"),False),
}
def wk_for(port,sk):
    df=pd.read_csv(f"{JUL}/{port}_{sk}.csv"); df['date']=pd.to_datetime(df['date'])
    sh=eng.SHOCKS['S1' if sk=='COVID' else 'S2']
    wk=eng.weekly(df); wk=eng.add_yoy(wk,'portcalls_container',sh['yoy_ref_year'],[]); return wk
WK={(p,s):wk_for(p,s) for p in ports for s in ('COVID','RedSea')}
def metrics(wk,w0,w1,mask):
    rc="portcalls_container_yoy_r4"
    win=wk[(wk.week_start>=pd.Timestamp(w0))&wk[rc].notna()].reset_index(drop=True)
    inwin=win[win.week_start<=pd.Timestamp(w1)]
    if mask: inwin=inwin[~inwin.iso_week.isin([51,52,53,1])]
    i=int(inwin[rc].idxmin()); tr=win.loc[i]; after=win.loc[i:].reset_index(drop=True)
    ht=tr[rc]+0.5*(1-tr[rc]); hl=after[after[rc]>=ht]
    hlw=int((hl.iloc[0].week_start-tr.week_start).days//7) if not hl.empty else None
    cens=hlw is None
    if cens: hlw=int((after.iloc[-1].week_start-tr.week_start).days//7)
    return round(100*(1-tr[rc]),1), hlw, str(tr.week_start.date()), cens
summary=[]
for tag,(w1,w2,mask) in VARIANTS.items():
    out=cond[['port','C1','C2','C3','C4','C5']].copy()
    dc,hc,tc,dr,hr,tr=[],[],[],[],[],[]
    for p in ports:
        d,h,t,c=metrics(WK[(p,'COVID')],*w1,mask); dc.append(d); hc.append(h); tc.append(t)
        d,h,t,c=metrics(WK[(p,'RedSea')],*w2,mask); dr.append(d); hr.append(h); tr.append(t)
    out['depth_cov']=dc; out['hl_cov']=hc; out['depth_red']=dr; out['hl_red']=hr
    out.to_csv(f"cond_JUL_{tag}.csv",index=False)
    out['trough_cov']=tc; out['trough_red']=tr; out.to_csv(f"cond_JUL_{tag}_full.csv",index=False)
# compare J0 to the July locked matrix
j0=pd.read_csv("cond_JUL_J0_exact.csv")
cmp=cond.merge(j0,on='port',suffixes=('_jul','_j0'))
same=((cmp.depth_cov_jul==cmp.depth_cov_j0)&(cmp.hl_cov_jul==cmp.hl_cov_j0)&(cmp.depth_red_jul==cmp.depth_red_j0)&(cmp.hl_red_jul==cmp.hl_red_j0))
print("J0 vs locked July matrix: identical ports =",same.sum(),"/22")
pd.set_option('display.width',250)
print(cmp.loc[~same,['port','depth_cov_jul','depth_cov_j0','hl_cov_jul','hl_cov_j0','depth_red_jul','depth_red_j0','hl_red_jul','hl_red_j0']].to_string(index=False))
