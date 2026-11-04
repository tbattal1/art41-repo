import pandas as pd, importlib.util, itertools, warnings; warnings.filterwarnings('ignore')
spec=importlib.util.spec_from_file_location("eng","src/art41_outcome.py"); eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
JUL='data/snapshots/july2026'
res=pd.read_csv('data/snapshots/july2026/ART41_outcome_results_july2026.csv')
def isoweek(d): y,w,_=pd.Timestamp(d).isocalendar(); return f"{y}-W{w:02d}"
cache={}
def wk_for(port,sk):
    if (port,sk) not in cache:
        df=pd.read_csv(f"{JUL}/{port}_{sk}.csv"); df['date']=pd.to_datetime(df['date']); cache[(port,sk)]=df
    return cache[(port,sk)]
def run(port,sk,col,w0,w1,trunc):
    df=wk_for(port,sk); df=df[df.date<=trunc]
    sh=dict(eng.SHOCKS['S1' if sk=='COVID' else 'S2']); sh['window']=(w0,w1)
    wk=eng.weekly(df); wk=eng.add_yoy(wk,col,sh['yoy_ref_year'],[])
    try: m=eng.metrics_yoy(wk,sh,col)
    except Exception as e: return None
    return (round(m['trough_ratio'],4), isoweek(m['trough_week']), m['half_life']['weeks_from_trough'])
for sk,starts,ends in [('COVID',['2020-01-01','2020-01-20','2020-02-01','2020-02-15','2020-03-01','2020-03-09','2020-03-11','2020-03-16'],
                                 ['2020-09-26','2020-09-30','2020-10-04','2020-10-11','2020-10-31','2020-12-31','2021-12-31']),
                       ('RedSea',['2023-10-01','2023-10-07','2023-11-01','2023-11-13','2023-11-19','2023-11-20','2023-12-01','2023-12-15','2023-12-18'],
                                 ['2024-09-26','2024-09-30','2024-10-06','2024-10-31','2024-12-31','2025-06-30'])]:
    sub=res[res.sok==sk]
    best=[]
    for w0,te in itertools.product(starts,ends):
        m=0; mh=0
        for _,r in sub.iterrows():
            out=run(r['vaka'],sk,r['metrik'],w0,'2025-12-31',te)
            if out and out[0]==round(r['dip_ratio'],4) and out[1]==r['dip_week']:
                m+=1
                if out[2]==r['halflife_weeks']: mh+=1
        best.append((m,mh,w0,te))
    best.sort(reverse=True)
    print(sk, 'n=',len(sub)); 
    for b in best[:8]: print('  ratio+dip match',b[0],'(+hl',b[1],') start',b[2],'trunc',b[3])

print("\n=== residuals ===")
for sk,w0,te in [('COVID','2020-01-01','2020-10-04'),('RedSea','2023-12-01','2024-09-26')]:
    sub=res[res.sok==sk]
    for _,r in sub.iterrows():
        out=run(r['vaka'],sk,r['metrik'],w0,'2025-12-31',te)
        ok=out and out[0]==round(r['dip_ratio'],4) and out[1]==r['dip_week']
        if not ok or (out and out[2]!=r['halflife_weeks']):
            print(sk,r['vaka'],r['metrik'],'| july',round(r['dip_ratio'],4),r['dip_week'],'ret',r['return_week'],'hl',r['halflife_weeks'],'| fit',out)
