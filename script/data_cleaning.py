import pandas as pd

"""nav = pd.read_csv("data/raw/02_nav_history.csv")
print(nav.head())
print(nav.columns)
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
print(nav.shape)
nav.to_csv("data/processed/clean_nav_history.csv", index=False)
print(nav.isnull().sum()) """

"""
tx = pd.read_csv("data/raw/08_investor_transactions.csv")
print(tx.columns)
tx["transaction_type"] = (tx["transaction_type"].str.strip().str.title())
valid = ["Sip", "Lumpsum", "Redemption"]
print(tx[~tx["transaction_type"].isin(valid)])
tx = tx[tx["amount_inr"] > 0]
tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])
print(tx["kyc_status"].value_counts())
tx.to_csv("data/processed/clean_transactions.csv", index=False)"""

"""perf = pd.read_csv("data/raw/07_scheme_performance.csv")
print(perf.columns)
metrics = ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct", "alpha", "beta", "sharpe_ratio", "sortino_ratio"]
for col in metrics:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")
anomalies = perf[(perf["expense_ratio_pct"] < 0.1) | (perf["expense_ratio_pct"] > 2.5)]
print(anomalies)
perf.to_csv("data/processed/clean_performance.csv", index=False) """


print(pd.read_csv("data/raw/01_fund_master.csv").columns.tolist())
print(pd.read_csv("data/raw/03_aum_by_fund_house.csv").columns.tolist())
print(pd.read_csv("data/raw/07_scheme_performance.csv").columns.tolist())
print(pd.read_csv("data/raw/08_investor_transactions.csv").columns.tolist())