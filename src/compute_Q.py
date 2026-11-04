"""ART-41 R1 — Q indicator (partner-region trade quotient) and E_C partner-weighted robustness.
Rules: exposure_rules_v1 §3.2 as refined by K17b (Euro-Med block; Gulf-plus; Russia/Belarus excluded from Asian reporters' far side).
"""
import json, glob, os, pandas as pd, numpy as np, country_converter as coco
cc = coco.CountryConverter()
ref = {x["PartnerCode"]: x for x in json.load(open("comtrade/partnerAreas.json"))["results"]}

def iso3(code):
    r = ref.get(code)
    if not r or r.get("isGroup") or code == 0: return None
    a3 = r.get("PartnerCodeIsoAlpha3")
    if not a3 or a3 in ("W00",) or len(a3) != 3: return None
    return a3

SPECIAL = {"S19":"Eastern Asia",      # Other Asia, nes = Taiwan Province of China (Comtrade 490)
           "E19":"Northern Europe",   # Europe nes -> treated as Europe
           "O19":"Melanesia",         # Oceania nes -> Oceania
           "F19":"Western Africa",    # Africa nes -> other (not far, not own)
           "A59":"South America",     # Americas nes -> other
           "A79":None, "_X":None, "X1":None, "XX":None}   # Asia nes / Areas nes -> unallocated
def region(a3):
    if a3 in SPECIAL: return SPECIAL[a3]
    return cc.convert(a3, to="UNregion", not_found=None)

EUROPE = {"Northern Europe","Western Europe","Southern Europe","Eastern Europe"}
GCC_PLUS = {"SAU","ARE","QAT","KWT","BHR","OMN","IRQ","IRN","YEM"}
LEVANT = {"TUR","CYP","SYR","LBN","ISR","PSE","JOR","GEO","ARM","AZE"}
OCEANIA = {"Australia and New Zealand","Melanesia","Micronesia","Polynesia"}
ASIA_FAR = {"Eastern Asia","South-eastern Asia","Southern Asia"}

def classify(reporter, a3):
    """returns 'own' | 'far' | 'other'"""
    reg = region(a3)
    if reporter in ("NLD","DEU","BEL","POL","ESP","GRC","MAR","TUR"):
        if reg in EUROPE or reg == "Northern Africa" or a3 in LEVANT: return "own"      # Euro-Med block
        if reg in ASIA_FAR or a3 in GCC_PLUS or reg == "Eastern Africa" or reg in OCEANIA: return "far"
        return "other"
    if reporter in ("CHN","KOR","SGP","MYS","LKA","ARE"):
        own = {"CHN":{"Eastern Asia","South-eastern Asia"},"KOR":{"Eastern Asia","South-eastern Asia"},
               "SGP":{"South-eastern Asia","Eastern Asia"},"MYS":{"South-eastern Asia","Eastern Asia"},
               "LKA":{"Southern Asia"},"ARE":{"Western Asia"}}[reporter]
        if reg in own: return "own"
        if (reg in EUROPE and a3 not in ("RUS","BLR")) or reg == "Northern Africa" or a3 in LEVANT: return "far"
        return "other"
    raise ValueError(reporter)

def load(reporter, period, cmd, flow):
    fn = f"comtrade/raw/{reporter}_{period}_{cmd}_{flow}.json"
    j = json.load(open(fn))
    return {d["partnerCode"]: d["primaryValue"] for d in j["data"]}

rows = []
for rep in ["NLD","DEU","BEL","POL","ESP","GRC","MAR","TUR","SGP","CHN","KOR","MYS","LKA","ARE"]:
    tot = {}; unalloc = 0.0
    for flow in ("M","X"):
        T = load(rep, 2023, "TOTAL", flow)
        minerals = {}
        for ch in ("25","26","27"):
            for k, v in load(rep, 2023, ch, flow).items(): minerals[k] = minerals.get(k, 0) + v
        for k, v in T.items():
            if k == 0: continue
            val = v - minerals.get(k, 0)
            a3 = iso3(k)
            if a3 is None or region(a3) is None: unalloc += val; continue
            tot[a3] = tot.get(a3, 0) + val
    far = sum(v for a3, v in tot.items() if classify(rep, a3) == "far")
    other = sum(v for a3, v in tot.items() if classify(rep, a3) == "other")
    own = sum(v for a3, v in tot.items() if classify(rep, a3) == "own")
    denom = far + other
    rows.append(dict(reporter=rep, far_bnUSD=round(far/1e9,1), other_bnUSD=round(other/1e9,1), own_bnUSD=round(own/1e9,1),
                     unallocated_bnUSD=round(unalloc/1e9,1), Q=round(far/denom, 3)))
Q = pd.DataFrame(rows)
print(Q.to_string(index=False))
Q.to_csv("Q_2023.csv", index=False)

# ---- E_C partner-weighted robustness: 2019 total-trade shares x partner 2020 mean stringency ----
ox = pd.read_csv("oxcgrt/OxCGRT_compact_national_v1.csv", usecols=["CountryCode","Jurisdiction","Date","StringencyIndex_Average"], low_memory=False)
ox = ox[ox.Jurisdiction=="NAT_TOTAL"]; ox["Date"] = pd.to_datetime(ox.Date.astype(str), format="%Y%m%d")
s20 = ox[(ox.Date>="2020-03-01")&(ox.Date<="2020-12-31")].groupby("CountryCode").StringencyIndex_Average.mean()
rows = []
for rep in ["NLD","DEU","BEL","POL","ESP","GRC","MAR","TUR","SGP","CHN","KOR","MYS","LKA","ARE","USA","CAN","BRA","COL","ZAF","NGA","AUS"]:
    w = {}
    for flow in ("M","X"):
        for k, v in load(rep, 2019, "TOTAL", flow).items():
            a3 = iso3(k)
            if a3 is None: continue
            w[a3] = w.get(a3, 0) + v
    tot = sum(w.values()); cov = 0; acc = 0
    for a3, v in w.items():
        if a3 in s20.index and not np.isnan(s20[a3]):
            acc += v * s20[a3]; cov += v
    rows.append(dict(reporter=rep, partner_weighted_S2020=round(acc/cov,1), weight_coverage=round(cov/tot,3)))
PW = pd.DataFrame(rows); print(); print(PW.to_string(index=False)); PW.to_csv("E_C_partner_weighted.csv", index=False)
