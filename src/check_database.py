import sqlite3
import pandas as pd
conn = sqlite3.connect("data/db/bluestock_mf.db")
tables = ["dim_fund", "fact_nav", "fact_transactions", "fact_performance", "fact_aum"]
for table in tables:
    query = f"""SELECT COUNT(*) AS rows FROM {table}"""
    result = pd.read_sql(query, conn)
    print("\n", table)
    print(result)
conn.close()