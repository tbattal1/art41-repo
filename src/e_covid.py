import pandas as pd, numpy as np, hashlib, datetime
f="oxcgrt/OxCGRT_compact_national_v1.csv"
sha=hashlib.sha256(open(f,'rb').read()).hexdigest()
df=pd.read_csv(f, usecols=["CountryName","CountryCode","Jurisdiction","Date","StringencyIndex_Average"], low_memory=False)
df=df[df.Jurisdiction=="NAT_TOTAL"]
df["Date"]=pd.to_datetime(df.Date.astype(str), format="%Y%m%d")
ports={"Rotterdam":"NLD","Hamburg":"DEU","Antwerp-Bruges":"BEL","Gdansk":"POL","Valencia":"ESP","Piraeus":"GRC",
"Tanger Med":"MAR","Mersin":"TUR","Singapore":"SGP","Shanghai":"CHN","Busan":"KOR","Port Klang":"MYS","Colombo":"LKA",
"Jebel Ali":"ARE","Los Angeles":"USA","New York/NJ":"USA","Vancouver":"CAN","Santos":"BRA","Cartagena":"COL","Durban":"ZAF","Lagos":"NGA","Melbourne":"AUS"}
w=df[(df.Date>="2020-03-01")&(df.Date<="2020-12-31")]
w2=df[(df.Date>="2020-03-01")&(df.Date<="2021-12-31")]
def calib(x,hi=70,mid=55,lo=40):
    # direct method logistic (Ragin): log-odds 3 at hi, 0 at mid, -3 at lo
    if x>=mid: lo_odds=3*(x-mid)/(hi-mid)
    else: lo_odds=3*(x-mid)/(mid-lo)
    return 1/(1+np.exp(-lo_odds))
rows=[]
for p,c in ports.items():
    s=w[w.CountryCode==c].StringencyIndex_Average
    s2=w2[w2.CountryCode==c].StringencyIndex_Average
    rows.append(dict(port=p,iso3=c,n_days_2020=s.notna().sum(),mean_2020=round(s.mean(),1),mean_2020_21=round(s2.mean(),1),
                     E_C=round(calib(s.mean()),2)))
out=pd.DataFrame(rows)
print(out.to_string(index=False))
print("\nabove crossover:", (out.E_C>0.5).sum(), "/22 ; min/median/max 2020:", out.mean_2020.min(), out.mean_2020.median(), out.mean_2020.max())
out.to_csv("E_C_oxcgrt_2020.csv",index=False)
open("oxcgrt/SNAPSHOT.txt","w").write(f"OxCGRT_compact_national_v1.csv downloaded {datetime.date.today()} from raw.githubusercontent.com/OxCGRT/covid-policy-dataset/main/data/ ; SHA-256 {sha}\n")
