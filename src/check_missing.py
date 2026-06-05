import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print(df.isnull().sum())

print("\nRows with missing values:\n")

print(df[df.isnull().any(axis=1)])