import pandas as pd

funds = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(funds["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = fund_codes - nav_codes

print("Missing codes:", len(missing))
print(missing)