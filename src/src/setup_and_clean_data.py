import os
import pandas as pd
from pathlib import Path

# --- Step 1: Dummy raw data ---
data = {
    "Benin": [
        "region,solar_capacity,year",
        "Benin,120,2020",
        "Benin,130,2021",
        "Benin,150,2022"
    ],
    "SierraLeone": [
        "region,solar_capacity,year",
        "Sierra Leone,80,2020",
        "Sierra Leone,90,2021",
        "Sierra Leone,95,2022"
    ],
    "Togo": [
        "region,solar_capacity,year",
        "Togo,60,2020",
        "Togo,75,2021",
        "Togo,85,2022"
    ]
}

# --- Step 2: Write raw CSV files ---
for country, lines in data.items():
    raw_dir = Path(f"data/{country}/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    raw_file = raw_dir / f"{country.lower().replace(' ', '_')}_raw.csv"
    with open(raw_file, "w") as f:
        f.write("\n".join(lines))
    print(f"[✓] Created raw file: {raw_file}")

# --- Step 3: Clean and save to processed folder ---
for country in data.keys():
    path = f"data/{country}"
    raw_file = Path(f"{path}/raw/{country.lower().replace(' ', '_')}_raw.csv")
    clean_file = Path(f"{path}/processed/{country.lower().replace(' ', '_')}_clean.csv")

    if not raw_file.exists():
        print(f"[!] Missing raw file: {raw_file}")
        continue

    # Load and clean
    df = pd.read_csv(raw_file)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df.columns = df.columns.str.strip().str.lower()

    # Save cleaned file
    clean_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(clean_file, index=False)
    print(f"[✓] Cleaned file saved: {clean_file}")
