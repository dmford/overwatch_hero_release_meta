# ==================================================
# Project: overwatch_hero_release_meta
# File: data_pull.py
# Purpose: Initial data pull + structure inspection
# Author: David Ford
# ==================================================


# ==================================================
# 0. IMPORTS
# ==================================================

import os
import json
import requests
import pandas as pd

from pathlib import Path
from datetime import datetime, timezone

# Clear terminal for clean reruns
os.system("cls" if os.name == "nt" else "clear")


# ==================================================
# 1. DIRECTORY SETUP
# ==================================================

RAW_DATA_DIR = Path("data/raw")
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# ==================================================
# 2. DATA SOURCE
# ==================================================

DATA_URL = (
    "https://raw.githubusercontent.com/hermit-crab/"
    "ow-winrates-faceted/master/winrate-data.js"
)


# ==================================================
# 3. PULL DATA
# ==================================================

print("\nPulling winrate-data.js...")

response = requests.get(DATA_URL)

print(f"HTTP status code: {response.status_code}")

response.raise_for_status()

raw_text = response.text


# ==================================================
# 4. SAVE RAW FILE
# ==================================================

raw_output_path = RAW_DATA_DIR / "winrate_data_raw.js"

with open(raw_output_path, "w", encoding="utf-8") as f:
    f.write(raw_text)

print(f"\nRaw JS data file saved to:\n{raw_output_path}")


# ==================================================
# 5. PARSE JSONP WRAPPER
# ==================================================

# The source file is not pure JSON. It is wrapped like:
# jsonp([...])
# So we remove the wrapper before using json.loads().
if not raw_text.startswith("jsonp("):
    raise ValueError("Unexpected file format: data does not start with jsonp(")

json_text = raw_text.removeprefix("jsonp(").removesuffix(")")

data = json.loads(json_text)


# ==================================================
# 6. INSPECT TOP-LEVEL STRUCTURE
# ==================================================

print("\n===== TOP-LEVEL OBJECT TYPE =====")
print(type(data))

print("\n===== NUMBER OF TOP-LEVEL ENTRIES =====")
print(len(data))

print("\n===== FIRST TOP-LEVEL ENTRY KEYS =====")
print(data[0].keys())


# ==================================================
# 7. FLATTEN HERO RATES WITH ENTRY METADATA
# ==================================================

rows = []

for entry_num, entry in enumerate(data):

    selected = entry.get("selected", {})
    rates = entry.get("rates", [])

    for hero_entry in rates:

        rows.append({
            "entry_num": entry_num,
            "timestamp": entry.get("_ts"),
            "source_url": entry.get("_url"),

            # Selected filters from the source
            "selected": selected,
            "selected_role": selected.get("role") if isinstance(selected, dict) else None,
            "selected_rank": selected.get("rank") if isinstance(selected, dict) else None,
            "selected_region": selected.get("region") if isinstance(selected, dict) else None,
            "selected_platform": selected.get("platform") if isinstance(selected, dict) else None,
            "selected_gamemode": selected.get("gamemode") if isinstance(selected, dict) else None,

            # Hero statistics
            "hero_id": hero_entry.get("id"),
            "hero_name": hero_entry.get("cells", {}).get("name"),
            "pickrate": hero_entry.get("cells", {}).get("pickrate"),
            "winrate": hero_entry.get("cells", {}).get("winrate"),
            "role": hero_entry.get("hero", {}).get("role"),
        })

df = pd.DataFrame(rows)

# Convert Unix timestamp to readable datetime
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    unit="s"
)


# ==================================================
# 8. SAVE FLATTENED DATA
# ==================================================

# Use actual pull date for archive filename.
# The source timestamp may refer to the upstream scrape date, not today's collection date.
pull_datetime = datetime.now(timezone.utc)
pull_date = pull_datetime.strftime("%Y_%m_%d")

df["pull_datetime_utc"] = pull_datetime
df["pull_date"] = pull_date

snapshot_date = pull_date

csv_output_path = (
    RAW_DATA_DIR /
    f"winrate_snapshot_{snapshot_date}.csv"
)

if csv_output_path.exists():
    print(f"\nSnapshot already exists for {snapshot_date}.")
    print("Skipping save to avoid duplicate data.")
    raise SystemExit

df.to_csv(csv_output_path, index=False)

print(f"\nFlattened CSV saved to:\n{csv_output_path}")


# ==================================================
# 9. INSPECT ENTRY-LEVEL METADATA
# ==================================================

entry_df = pd.DataFrame([
    {
        "entry_num": i,
        "timestamp": entry.get("_ts"),
        "source_url": entry.get("_url"),
        "selected": entry.get("selected"),
        "num_heroes": len(entry.get("rates", [])),
    }
    for i, entry in enumerate(data)
])

entry_output_path = RAW_DATA_DIR / "entry_metadata.csv"
entry_df.to_csv(entry_output_path, index=False)

print(f"\nEntry metadata saved to:\n{entry_output_path}")

print("\n===== ENTRY METADATA =====")
print(entry_df.head(20))

print("\n===== SELECTED FILTER VALUES =====")
print(entry_df["selected"].head(20).to_string(index=False))


# ==================================================
# 10. INSPECT DATAFRAME
# ==================================================

print("\n===== TOP 10 ROWS =====")
print(df.head(10))

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATAFRAME SHAPE =====")
print(df.shape)

print("\n===== ROLE COUNTS =====")
print(df["role"].value_counts(dropna=False))

print("\n===== UNIQUE HERO COUNT =====")
print(df["hero_id"].nunique())

print("\n===== HERO NAMES =====")
print(sorted(df["hero_name"].dropna().unique()))

print("\n===== TIMESTAMP VALUES =====")
print(df["timestamp"].drop_duplicates().head(20).to_string(index=False))

print("\n===== SOURCE URL VALUES =====")
print(df["source_url"].drop_duplicates().head(20).to_string(index=False))