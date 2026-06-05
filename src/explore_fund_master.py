import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nNumber of Funds:")
print(len(df))

print("\nFund Houses:")
print(df["fund_house"].value_counts())

print("\nCategories:")
print(df["category"].value_counts())

print("\nSub Categories:")
print(df["sub_category"].value_counts())

print("\nRisk Categories:")
print(df["risk_category"].value_counts())