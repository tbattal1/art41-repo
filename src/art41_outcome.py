#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ART-41 — PortWatch Outcome Hesabı v5.3 (Ş1/Ş2)
=============================================
v3 = v2 (level+yoy iki tanim) + VERI DONDURMA DISIPLINI.

NEDEN v3: PortWatch canli API gecmise donuk veri duzeltir (backfill).
Ayni komut iki gun arayla farkli sonuc verebilir (Rotterdam 07.07: sustained
null -> 2021-06-14 degisimi bunu kanitladi). Cozum: ham veriyi BIR KEZ cek,
diske dondur (snapshot), TUM analizleri o dondurulmus dosyadan calistir.

AKIS:
  1) Snapshot yoksa API'den ceker + art41_snapshots/{portid}_{shock}_raw_{YYYYMMDD}.csv yazar
  2) Snapshot varsa API'ye HIC gitmez, dondurulmus dosyadan okur (deterministik)
  3) Her iki tanimi (level + yoy) hesaplar, yan yana raporlar

Kullanim:
  Ilk cekim (snapshot olusturur):
    python art41_outcome.py --portid port1114 --portname Rotterdam --shock S1
  Tekrar (ayni snapshot'tan, agdan bagimsiz, ayni sonuc):
    python art41_outcome.py --portid port1114 --shock S1
  Belirli snapshot'i sabitle (repro icin):
    python art41_outcome.py --portid port1114 --shock S1 --snapshot art41_snapshots/port1114_S1_raw_20260707.csv
  Snapshot'i yenile (API'yi yeniden cek, yeni tarihli dosya):
    python art41_outcome.py --portid port1114 --shock S1 --refresh

Gereksinimler: pip install pandas requests
Cikti (./art41_out/): {portid}_{shock}_weekly.csv | _metrics.json | _log.txt
Snapshot (./art41_snapshots/): {portid}_{shock}_raw_{YYYYMMDD}.csv  <- GitHub'a bununla commit
"""
import argparse, json, hashlib, sys, os, glob
from datetime import datetime, timezone

import pandas as pd

API_URL = ("https://services9.arcgis.com/weJ1QsnbMYJlCHdG/ArcGIS/rest/services/"
           "Daily_Ports_Data/FeatureServer/0/query")

# v5.3 (Nov 2026, revision R1): measurement windows = acute-phase windows of codebook rule K22; K24 pre-shock-level rule.
#   S1 COVID   : 2020-01-01 .. 2020-09-30  (demand-collapse phase; Q4-2020 onward = congestion regime)
#   S2 Red Sea : 2023-11-19 .. 2024-11-18  (12 months from the Galaxy Leader hijack, 19 Nov 2023)
# The submitted version (Jul 2026) de facto used 2020-02-24..2020-10-04 and 2023-11-26..2024-09-26
# (recovered empirically; see codebook K22 and src/grid.py). series_* ranges are unchanged.
SHOCKS = {
    "S1": {"baseline": ("2019-01-01", "2019-12-31"),
           "window": ("2020-01-01", "2020-09-30"),
           "series_start": "2019-01-01", "series_end": "2022-01-09",
           "yoy_ref_year": 2019},
    "S2": {"baseline": ("2023-01-01", "2023-09-30"),
           "window": ("2023-11-19", "2024-11-18"),
           "series_start": "2021-01-01", "series_end": "2025-07-06",
           "yoy_ref_year": 2022},
}
RECOVERY_FRAC = 0.95
SUSTAIN_WEEKS = 4
ROLL_W = 4
SNAP_DIR = "art41_snapshots"


def sha12(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:12]


def fetch_api(portid, start, end, log):
    import requests
    rows, offset = [], 0
    where = f"portid='{portid}' AND date>=timestamp '{start}' AND date<=timestamp '{end}'"
    while True:
        params = {"where": where,
                  "outFields": "date,portid,portcalls,portcalls_container,portcalls_cargo,portcalls_tanker",
                  "orderByFields": "date", "returnGeometry": "false",
                  "resultOffset": offset, "resultRecordCount": 2000, "f": "json"}
        js = None
        for attempt in range(8):                      # v5.1: retry on transient ArcGIS errors (HTTP 400 "Invalid URL", 429, 5xx)
            try:
                r = requests.get(API_URL, params=params, timeout=120)
                r.raise_for_status()
                js = r.json()
                if "error" in js:
                    raise RuntimeError(js["error"])
                break
            except Exception as e:
                if attempt == 7:
                    raise
                import time; wait = 15 * (attempt + 1)
                log.append(f"API retry {attempt+1} after error: {str(e)[:80]} (sleep {wait}s)")
                time.sleep(wait)
        feats = js.get("features", [])
        rows += [f["attributes"] for f in feats]
        log.append(f"API batch offset={offset} -> {len(feats)}")
        if len(feats) < 2000:
            break
        offset += 2000
    df = pd.DataFrame(rows)
    if df.empty:
        raise RuntimeError(f"API bos: portid={portid} {start}..{end}")
    df["date"] = pd.to_datetime(df["date"], unit="ms", utc=True).dt.tz_localize(None)
    return df


def get_data(args, shock, log):
    """Snapshot-first veri edinimi. Doner: (df, snapshot_yolu, kaynak_str)."""
    os.makedirs(SNAP_DIR, exist_ok=True)
    start, end = shock["series_start"], shock["series_end"]

    # 1) Kullanici belirli snapshot verdiyse onu kullan (en yuksek oncelik)
    if args.snapshot:
        df = pd.read_csv(args.snapshot)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        log.append(f"SNAPSHOT (sabit): {args.snapshot} sha256[:12]={sha12(args.snapshot)}")
        return df, args.snapshot, f"snapshot:{os.path.basename(args.snapshot)}"

    pattern = f"{SNAP_DIR}/{args.portid}_{args.shock}_raw_*.csv"
    existing = sorted(glob.glob(pattern))

    # 2) refresh degilse ve snapshot varsa: en yeni snapshot'tan oku (API'ye gitme)
    if existing and not args.refresh:
        latest = existing[-1]
        df = pd.read_csv(latest)
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        log.append(f"SNAPSHOT (mevcut, deterministik): {latest} sha256[:12]={sha12(latest)}")
        log.append("API'ye GIDILMEDI — sonuc tekrarlanabilir.")
        return df, latest, f"snapshot:{os.path.basename(latest)}"

    # 3) snapshot yok VEYA refresh istendi: API'den cek + dondur
    df = fetch_api(args.portid, start, end, log)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    snap = f"{SNAP_DIR}/{args.portid}_{args.shock}_raw_{stamp}.csv"
    keep = [c for c in ["date", "portid", "portcalls", "portcalls_container",
                        "portcalls_cargo", "portcalls_tanker"] if c in df.columns]
    df[keep].to_csv(snap, index=False)
    log.append(f"SNAPSHOT (YENI olusturuldu): {snap} sha256[:12]={sha12(snap)}")
    log.append(">> Bu dosyayi GitHub'a commit et; analiz bundan sonra hep buradan kosar.")
    return df, snap, f"API->snapshot:{os.path.basename(snap)}"


def weekly(df):
    df = df.copy()
    df = df[df["date"].notna()]
    iso = df["date"].dt.isocalendar()
    df["iso_year"], df["iso_week"] = iso["year"].astype(int), iso["week"].astype(int)
    g = (df.groupby(["iso_year", "iso_week"])
           .agg(days=("date", "nunique"), week_start=("date", "min"),
                portcalls=("portcalls", "sum"),
                portcalls_container=("portcalls_container", "sum"))
           .reset_index())
    return g[g["days"] == 7].sort_values("week_start").reset_index(drop=True)


def add_yoy(wk, col, ref_year, log):
    ref = wk[wk["iso_year"] == ref_year].set_index("iso_week")[col]
    def rv(w):
        if w in ref.index: return ref.loc[w]
        if w == 53 and 52 in ref.index: return ref.loc[52]
        return None
    out, w53 = [], False
    for _, r in wk.iterrows():
        if r["iso_year"] <= ref_year:
            out.append(None); continue
        v = rv(r["iso_week"])
        if r["iso_week"] == 53: w53 = True
        out.append(float(r[col]) / float(v) if v and v > 0 else None)
    wk[f"{col}_yoy"] = out
    wk[f"{col}_yoy_r{ROLL_W}"] = pd.Series(out, dtype="float64").rolling(ROLL_W, min_periods=ROLL_W).mean()
    if w53: log.append(f"NOT: ISO W53->W52 eslendi ({col})")
    return wk


def wk_out(row, t0):
    if row is None: return {"week": None, "weeks_from_trough": None}
    return {"week": str(row["week_start"].date()),
            "weeks_from_trough": int((row["week_start"] - t0).days // 7)}


def _level_core(wk_win, base_mean, col, valcol, tag, exclude_isoweeks=None):
    """Ortak LEVEL cekirdegi. valcol = seviyeyi tasiyan sutun (col ya da col_adj)."""
    thr = RECOVERY_FRAC * base_mean
    win = wk_win.copy()
    search = win if not exclude_isoweeks else win[~win["iso_week"].isin(exclude_isoweeks)]
    i = search[valcol].idxmin()
    tr = win.loc[i]
    after = win.loc[i:].reset_index(drop=True)
    ft = after[after[valcol] >= thr]
    vals = (after[valcol] >= thr).tolist()
    sus = next((after.iloc[j] for j in range(len(vals)-SUSTAIN_WEEKS+1)
                if all(vals[j:j+SUSTAIN_WEEKS])), None)
    ht = float(tr[valcol]) + 0.5*(base_mean-float(tr[valcol]))
    hl = after[after[valcol] >= ht]
    return {"definition": tag,
            "baseline_weekly_mean": round(base_mean, 2),
            "trough_week": str(tr["week_start"].date()),
            "trough_value": round(float(tr[valcol]), 2),
            "drop_depth_pct": round(100*(1-float(tr[valcol])/base_mean), 2),
            "recovery_first_touch": wk_out(None if ft.empty else ft.iloc[0], tr["week_start"]),
            "recovery_sustained_4wk": wk_out(sus, tr["week_start"]),
            "half_life": wk_out(None if hl.empty else hl.iloc[0], tr["week_start"])}


def metrics_level(wk, shock, col):
    """Uc LEVEL varyanti dondurur: raw / mask (yil sonu haftalari dip aramasindan cikar) /
       seasonal (mevsim profiliyle duzeltilmis seviye)."""
    b0, b1 = pd.Timestamp(shock["baseline"][0]), pd.Timestamp(shock["baseline"][1])
    w0, w1 = pd.Timestamp(shock["window"][0]), pd.Timestamp(shock["window"][1])
    base = wk[(wk["week_start"] >= b0) & (wk["week_start"] <= b1)]
    win_full = wk[wk["week_start"] >= w0]
    win = win_full[win_full["week_start"] <= w1].reset_index(drop=True)
    if base.empty or win.empty:
        return {"error": "taban/pencere bos"}
    base_mean = float(base[col].mean())

    out = {}
    # (raw) — v3 ile ayni: ham seviye, tum haftalar dip adayi
    out["raw"] = _level_core(win, base_mean, col, col,
                             "LEVEL-raw (ham seviye; mevsimsellige acik)")
    # (mask) — yil sonu ISO 51,52,53,1 haftalarini DIP ARAMASINDAN disla (seviye ayni kalir)
    out["mask"] = _level_core(win, base_mean, col, col,
                              "LEVEL-mask (dip aramasi ISO 51-53,1 haric)",
                              exclude_isoweeks={51, 52, 53, 1})
    # (seasonal) — mevsim profili: taban yilinin her ISO haftasindaki seviye / taban ortalamasi
    prof = base.groupby("iso_week")[col].mean()
    prof_ratio = (prof / base_mean).to_dict()   # hafta -> mevsim carpani
    wtmp = win.copy()
    wtmp["season_factor"] = wtmp["iso_week"].map(lambda w: prof_ratio.get(w, prof_ratio.get(52 if w==53 else w, 1.0)))
    # duzeltilmis seviye = ham / mevsim carpani -> mevsim etkisi notrlenir, seviye olcegi korunur
    wtmp[col+"_adj"] = wtmp[col] / wtmp["season_factor"].replace(0, 1.0)
    out["seasonal"] = _level_core(wtmp, base_mean, col, col+"_adj",
                                  "LEVEL-seasonal (mevsim profiliyle duzeltilmis; taban yili "
                                  + str(shock["yoy_ref_year"]) + " profili)")
    return out


PRE_WEEKS, PRE_TOL, EARLY_WEEKS = 8, 0.15, 4     # K24 pre-shock-level rule (v5.3)

def metrics_yoy(wk, shock, col):
    rc = f"{col}_yoy_r{ROLL_W}"
    w0, w1 = pd.Timestamp(shock["window"][0]), pd.Timestamp(shock["window"][1])
    win = wk[(wk["week_start"] >= w0) & wk[rc].notna()].reset_index(drop=True)
    if win.empty: raise RuntimeError("yoy penceresi bos")
    inwin = win[win["week_start"] <= w1]; i = int(inwin[rc].idxmin()); tr = win.loc[i]
    after = win.loc[i:].reset_index(drop=True)
    ft = after[after[rc] >= RECOVERY_FRAC]; vals = (after[rc] >= RECOVERY_FRAC).tolist()
    sus = next((after.iloc[j] for j in range(len(vals)-SUSTAIN_WEEKS+1)
                if all(vals[j:j+SUSTAIN_WEEKS])), None)
    # K24 (codebook B.9): pre-shock level = mean ratio over the 8 weeks before the window. If it deviates from
    # 1 by more than 15 % and the trough falls in the first 4 window weeks, the decline pre-dates the shock;
    # depth and half-life are then measured against the pre-shock level. Not applicable where no pre-window
    # ratios exist (COVID window: reference year 2019 = series start).
    pre_s = wk[(wk["week_start"] < w0) & (wk["week_start"] >= w0 - pd.Timedelta(weeks=PRE_WEEKS))][rc].dropna()
    pre = float(pre_s.mean()) if len(pre_s) else None
    early = (tr["week_start"] - w0).days // 7 < EARLY_WEEKS
    k24 = pre is not None and abs(pre - 1.0) > PRE_TOL and early
    if k24:
        depth = max(0.0, 100*(1 - float(tr[rc])/pre)); ht = float(tr[rc]) + 0.5*(pre - float(tr[rc]))
    else:
        depth = 100*(1 - float(tr[rc])); ht = float(tr[rc]) + 0.5*(1.0 - float(tr[rc]))
    hl = after[after[rc] >= ht]
    hl_out = wk_out(None if hl.empty else hl.iloc[0], tr["week_start"])
    if k24 and depth == 0: hl_out = {"week": None, "weeks_from_trough": 0}
    return {"definition": f"YOY ayni-hafta orani, {ROLL_W}h yuvarlanan (ref {shock['yoy_ref_year']}; mevsimsellik-arindirilmis)",
            "trough_week": str(tr["week_start"].date()), "trough_ratio": round(float(tr[rc]), 4),
            "pre_shock_level": None if pre is None else round(pre, 4), "k24_applied": bool(k24),
            "drop_depth_pct": round(depth, 2),
            "recovery_first_touch": wk_out(None if ft.empty else ft.iloc[0], tr["week_start"]),
            "recovery_sustained_4wk": wk_out(sus, tr["week_start"]),
            "half_life": hl_out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--portid", required=True)
    ap.add_argument("--portname", default="")
    ap.add_argument("--shock", choices=["S1", "S2"], required=True)
    ap.add_argument("--snapshot", default=None, help="Belirli dondurulmus CSV'yi sabitle")
    ap.add_argument("--refresh", action="store_true", help="API'yi yeniden cek, yeni snapshot yaz")
    ap.add_argument("--outdir", default="art41_out")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    shock = SHOCKS[args.shock]
    log = [f"ART-41 outcome v5.3 | {datetime.now(timezone.utc).isoformat()}",
           f"portid={args.portid} shock={args.shock}",
           f"taban {shock['baseline']} | sok {shock['window']} | yoy_ref {shock['yoy_ref_year']}",
           f"esik={RECOVERY_FRAC} sustain={SUSTAIN_WEEKS}h roll={ROLL_W}h"]
    if args.shock == "S2":
        log.append("S2 yoy referans yili=2022 (Kizildeniz-oncesi son temiz yil; Codebook Bolum B karari)")

    df, snap, source = get_data(args, shock, log)
    wk = weekly(df)
    log.append(f"ISO-haftalik: {len(wk)} tam hafta ({wk['week_start'].min().date()} -> {wk['week_start'].max().date()})")

    results = {}
    for col in ("portcalls", "portcalls_container"):
        wk = add_yoy(wk, col, shock["yoy_ref_year"], log)
        entry = {}
        try: entry["level"] = metrics_level(wk, shock, col)
        except Exception as e: entry["level"] = {"error": str(e)}
        try: entry["yoy"] = metrics_yoy(wk, shock, col)
        except Exception as e: entry["yoy"] = {"error": str(e)}
        results[col] = entry

    stem = f"{args.portid}_{args.shock}"
    wk.to_csv(f"{args.outdir}/{stem}_weekly.csv", index=False)
    meta = {"portid": args.portid, "portname": args.portname, "shock": args.shock,
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "codebook_version": "v2.9", "script_version": "v5.3",
            "data_source": source, "snapshot_file": snap, "snapshot_sha256_12": sha12(snap),
            "results": results}
    with open(f"{args.outdir}/{stem}_metrics.json", "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
    with open(f"{args.outdir}/{stem}_log.txt", "w") as f:
        f.write("\n".join(log) + "\n")
    print(json.dumps(meta, indent=2, ensure_ascii=False))
    print(f"\nSnapshot: {snap}")
    print(f"Dosyalar: {args.outdir}/{stem}_weekly.csv | _metrics.json | _log.txt")


if __name__ == "__main__":
    sys.exit(main())
