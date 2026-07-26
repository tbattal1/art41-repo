#!/usr/bin/env python3
"""
EU ETS EUA Günlük Fiyat Verisi İndirici
Kaynak: Investing.com / yfinance (ICE Carbon Futures)
Dönem: 2024-01-01 → 2025-09-30
Gçktı: eu_ets_eua_daily_2024_2025.csv
"""

import requests
import pandas as pd
import json, time


def fetch_yfinance_eua(start="2024-01-01", end="2025-09-30"):
    """
    yfinance ile ICE EUA CFI2 front-month futures çeker.
    Ticker: CFI2Z4.L (2024), CFI2Z5.L (2025)
    """
    try:
        import yfinance as yf
        frames = []
        for ticker in ["CFI2Z4.L", "CFI2Z5.L"]:
            t = yf.Ticker(ticker)
            df = t.history(start=start, end=end, interval="1d")
            if len(df) > 0:
                df = df[["Close"]].reset_index()
                df.columns = ["date", "close_eur_tonne"]
                df["date"] = df["date"].dt.strftime("%Y-%m-%d")
                df["source"] = f"{ticker} via yfinance"
                frames.append(df)
                print(f"✅ {ticker}: {len(df)} gün")
        if frames:
            combined = pd.concat(frames).drop_duplicates("date").sort_values("date")
            return combined
    except Exception as e:
        print(f"yfinance hatası: {e}")
    return None


def fetch_investing_eua(start="2024-01-01", end="2025-09-30"):
    """
    Investing.com non-public API üzerinden EUA (pair_id=8833) verisi çeker.
    Oturum açık olmalıdır; gerekirse tarayıcıdan cookie kopyalayın.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.investing.com/commodities/carbon-emissions-historical-data",
    }
    url = "https://api.investing.com/api/financials/historical/chart/"
    params = {
        "pair_id": "8833",
        "period": "Daily",
        "start_date": start,
        "end_date": end,
    }
    try:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        rows = []
        for item in data.get("data", []):
            rows.append({
                "date":   pd.to_datetime(item[0], unit="ms").strftime("%Y-%m-%d"),
                "open":   item[1],
                "high":   item[2],
                "low":    item[3],
                "close_eur_tonne": item[4],
                "volume": item[5] if len(item) > 5 else None,
                "source": "investing.com/Carbon-Emissions pair_id=8833"
            })
        return pd.DataFrame(rows)
    except Exception as e:
        print(f"investing.com API hatası: {e}")
    return None


if __name__ == "__main__":
    print("EU ETS EUA Günlük Veri İndirici")
    print("=" * 40)

    df = fetch_yfinance_eua()

    if df is None or len(df) == 0:
        print("\nInvesting.com deneniyor...")
        df = fetch_investing_eua()

    if df is not None and len(df) > 0:
        out = "eu_ets_eua_daily_2024_2025.csv"
        df.to_csv(out, index=False)
        print(f"\n✅ Kaydedildi: {out} ({len(df)} iş günü)")
        print(df.head())
    else:
        print("\n❌ Otomatik çekme başarısız.")
        print("Manuel alternatif:")
        print("  EEX: https://www.eex.com/en/market-data/environmental-markets/")
        print("  Investing.com: https://www.investing.com/commodities/carbon-emissions-historical-data")
        print("  ICE: https://www.theice.com/products/197/EUA-Future")
