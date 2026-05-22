"""Download daily NASA POWER data for the Florida climate dashboard.

Output: data/florida_nasa_power_daily.csv
"""
from __future__ import annotations

from datetime import date
from pathlib import Path
import time

import pandas as pd
import requests

CITIES = [
    {"city": "Miami", "lat": 25.7617, "lon": -80.1918},
    {"city": "Tampa", "lat": 27.9506, "lon": -82.4572},
    {"city": "Orlando", "lat": 28.5383, "lon": -81.3792},
    {"city": "Jacksonville", "lat": 30.3322, "lon": -81.6557},
    {"city": "Fort Myers / Cape Coral", "lat": 26.6406, "lon": -81.8723},
]

PARAMETERS = [
    "T2M",
    "T2M_MAX",
    "T2M_MIN",
    "PRECTOTCORR",
    "RH2M",
    "WS2M",
    "ALLSKY_SFC_SW_DWN",
    "PS",
    "T2MDEW",
]

API_BASE = "https://power.larc.nasa.gov/api/temporal/daily/point"
START_DATE = "20150101"
END_DATE = date.today().strftime("%Y%m%d")
OUTPUT_PATH = Path("data/florida_nasa_power_daily.csv")


def fetch_city(city_info: dict) -> pd.DataFrame:
    params = {
        "parameters": ",".join(PARAMETERS),
        "community": "AG",
        "longitude": city_info["lon"],
        "latitude": city_info["lat"],
        "start": START_DATE,
        "end": END_DATE,
        "format": "JSON",
    }
    response = requests.get(API_BASE, params=params, timeout=90)
    response.raise_for_status()
    payload = response.json()
    parameter_data = payload["properties"]["parameter"]

    first_parameter = PARAMETERS[0]
    records = []
    for yyyymmdd in sorted(parameter_data[first_parameter].keys()):
        dt = pd.to_datetime(yyyymmdd, format="%Y%m%d")
        row = {
            "date": dt.strftime("%Y-%m-%d"),
            "city": city_info["city"],
            "latitude": city_info["lat"],
            "longitude": city_info["lon"],
            "year": int(dt.year),
            "month": int(dt.month),
            "month_name": dt.strftime("%b"),
            "year_month": dt.strftime("%Y-%m"),
        }
        for parameter in PARAMETERS:
            value = parameter_data.get(parameter, {}).get(yyyymmdd)
            if value in (-999, -999.0, None):
                value = pd.NA
            row[parameter] = value
        records.append(row)
    return pd.DataFrame(records)


def main() -> pd.DataFrame:
    frames = []
    for i, city_info in enumerate(CITIES, start=1):
        print(f"Downloading {city_info['city']} ({i}/{len(CITIES)})...")
        frames.append(fetch_city(city_info))
        time.sleep(0.3)

    df = pd.concat(frames, ignore_index=True)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(df):,} rows to {OUTPUT_PATH}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    return df


if __name__ == "__main__":
    main()
