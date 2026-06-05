import pandas as pd
import os

report = []

DATA_PATH = "data/raw"

files = sorted([
    f for f in os.listdir(DATA_PATH)
    if f.endswith(".csv")
])

for file in files:

    df = pd.read_csv(os.path.join(DATA_PATH,file))

    report.append({
        "file": file,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum()
    })

quality = pd.DataFrame(report)

quality.to_csv(
    "reports/data_quality_report.csv",
    index=False
)

print(quality)