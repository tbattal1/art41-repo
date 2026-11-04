import sys, pandas as pd, csv, importlib.util
spec=importlib.util.spec_from_file_location("eng","src/art41_outcome.py"); eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
JUL='data/snapshots/july2026'
res=pd.read_csv('data/snapshots/july2026/ART41_outcome_results_july2026.csv')
def isoweek(d): 
    d=pd.Timestamp(d); y,w,_=d.isocalendar(); return f"{y}-W{w:02d}"
def run(port,shockname,col,trunc=None,start=None):
    sh=eng.SHOCKS['S1' if shockname=='COVID' else 'S2']
    df=pd.read_csv(f"{JUL}/{port}_{shockname}.csv"); df['date']=pd.to_datetime(df['date'])
    if start: df=df[df.date>=start]
    if trunc: df=df[df.date<=trunc]
    wk=eng.weekly(df); log=[]
    wk=eng.add_yoy(wk,col,sh['yoy_ref_year'],log)
    m=eng.metrics_yoy(wk,sh,col)
    return (round(m['trough_ratio'],4), m['drop_depth_pct'], isoweek(m['trough_week']),
            m['recovery_first_touch']['weeks_from_trough'], m['half_life']['weeks_from_trough'])
rows=[]
for _,r in res.iterrows():
    port,sk,col=r['vaka'],r['sok'],r['metrik']
    jul=(round(r['dip_ratio'],4), r['depth_pct'], r['dip_week'], None, r['halflife_weeks'])
    full=run(port,sk,col)
    tr=run(port,sk,col,trunc='2020-09-26' if sk=='COVID' else '2024-09-26')
    rows.append(dict(port=port,shock=sk,col=col,jul_ratio=jul[0],jul_dip=jul[2],jul_hl=jul[4],jul_ret=r['return_week'],
        full_ratio=full[0],full_dip=full[2],full_hl=full[4],full_ret=full[3],
        trunc_ratio=tr[0],trunc_dip=tr[2],trunc_hl=tr[4],trunc_ret=tr[3]))
out=pd.DataFrame(rows)
out['match_full']=(out.jul_ratio==out.full_ratio)&(out.jul_dip==out.full_dip)
out['match_trunc']=(out.jul_ratio==out.trunc_ratio)&(out.jul_dip==out.trunc_dip)
pd.set_option('display.width',250); pd.set_option('display.max_rows',200)
print(out[['port','shock','col','jul_ratio','jul_dip','jul_hl','full_ratio','full_dip','full_hl','trunc_ratio','trunc_dip','trunc_hl','match_full','match_trunc']].to_string())
print('\nmatch_full:',out.match_full.sum(),'/',len(out),'  match_trunc:',out.match_trunc.sum(),'/',len(out))
out.to_csv('results/july_repro.csv',index=False)
