import os

# Country raw data
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

# Create raw folders and write files
for country, lines in data.items():
    raw_dir = os.path.join("data", country, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    
    file_path = os.path.join(raw_dir, f"{country.lower().replace(' ', '_')}_raw.csv")
    with open(file_path, "w") as f:
        f.write("\n".join(lines))
    print(f"[✓] Created {file_path}")
