import pandas as pd
import os

DATA_PATH = "data/raw"

files = sorted([
    f for f in os.listdir(DATA_PATH)
    if f.endswith(".csv")
])

for file in files:

    print("\n" + "="*70)
    print(file)
    print("="*70)

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 3 Rows:")
    print(df.head(3))