# Data Dictionary

## dim_fund

Source: 01_fund_master.csv

Purpose: Master reference table containing details of all mutual fund schemes.

| Column             | Data Type | Description                                        |
| ------------------ | --------- | -------------------------------------------------- |
| amfi_code          | TEXT      | Unique AMFI scheme identifier                      |
| fund_house         | TEXT      | Mutual fund company (AMC)                          |
| scheme_name        | TEXT      | Official scheme name                               |
| category           | TEXT      | Fund category (Equity, Debt, Hybrid, etc.)         |
| sub_category       | TEXT      | Sub-category (Large Cap, Mid Cap, Small Cap, etc.) |
| plan               | TEXT      | Direct or Regular plan                             |
| launch_date        | DATE      | Fund launch date                                   |
| benchmark          | TEXT      | Benchmark index used for comparison                |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)                           |
| exit_load_pct      | REAL      | Exit load charged on redemption                    |
| min_sip_amount     | REAL      | Minimum SIP investment amount                      |
| min_lumpsum_amount | REAL      | Minimum lumpsum investment amount                  |
| fund_manager       | TEXT      | Fund manager name                                  |
| risk_category      | TEXT      | Risk classification                                |
| sebi_category_code | TEXT      | SEBI category code                                 |

---

## fact_nav

Source: 02_nav_history.csv

Purpose: Stores historical Net Asset Value (NAV) for all mutual fund schemes.

| Column    | Data Type | Description                       |
| --------- | --------- | --------------------------------- |
| amfi_code | TEXT      | Mutual fund scheme identifier     |
| nav_date  | DATE      | NAV date                          |
| nav       | REAL      | Net Asset Value on the given date |

---

## fact_transactions

Source: 08_investor_transactions.csv

Purpose: Stores investor transaction history.

| Column             | Data Type | Description                     |
| ------------------ | --------- | ------------------------------- |
| investor_id        | TEXT      | Unique investor identifier      |
| transaction_date   | DATE      | Date of transaction             |
| amfi_code          | TEXT      | Fund invested in                |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption     |
| amount_inr         | REAL      | Transaction amount in INR       |
| state              | TEXT      | Investor state                  |
| city               | TEXT      | Investor city                   |
| city_tier          | TEXT      | T30 or B30 classification       |
| age_group          | TEXT      | Investor age category           |
| gender             | TEXT      | Investor gender                 |
| annual_income_lakh | REAL      | Annual income in lakhs          |
| payment_mode       | TEXT      | UPI, Net Banking, Mandate, etc. |
| kyc_status         | TEXT      | Verified or Pending             |

---

## fact_performance

Source: 07_scheme_performance.csv

Purpose: Stores risk and performance metrics for mutual fund schemes.

| Column             | Data Type | Description                       |
| ------------------ | --------- | --------------------------------- |
| amfi_code          | TEXT      | Mutual fund identifier            |
| return_1yr_pct     | REAL      | One-year return (%)               |
| return_3yr_pct     | REAL      | Three-year CAGR (%)               |
| return_5yr_pct     | REAL      | Five-year CAGR (%)                |
| benchmark_3yr_pct  | REAL      | Benchmark 3-year return (%)       |
| alpha              | REAL      | Excess return over benchmark      |
| beta               | REAL      | Market sensitivity measure        |
| sharpe_ratio       | REAL      | Risk-adjusted return metric       |
| sortino_ratio      | REAL      | Downside-risk-adjusted return     |
| std_dev_ann_pct    | REAL      | Annualized volatility (%)         |
| max_drawdown_pct   | REAL      | Maximum portfolio decline (%)     |
| aum_crore          | REAL      | Assets Under Management (crore ₹) |
| expense_ratio_pct  | REAL      | Expense ratio (%)                 |
| morningstar_rating | INTEGER   | Morningstar rating (1–5)          |
| risk_grade         | TEXT      | Risk classification               |

---

## fact_aum

Source: 03_aum_by_fund_house.csv

Purpose: Stores Assets Under Management (AUM) information for fund houses.

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Asset Management Company  |
| aum_lakh_crore | REAL      | AUM in lakh crore rupees  |
| aum_crore      | REAL      | AUM in crore rupees       |
| num_schemes    | INTEGER   | Number of schemes managed |
