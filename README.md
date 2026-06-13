# 📊 Mutual Fund Analytics Platform

An end-to-end Mutual Fund Analytics platform built using Python, SQLite, Jupyter Notebook and Power BI to analyze fund performance, investor behavior, portfolio risk, and industry trends.

---

## Project Overview

The Indian Mutual Fund industry has experienced significant growth in Assets Under Management (AUM), SIP inflows, and investor participation. This project provides a complete analytics solution that:

- Ingests and validates mutual fund datasets
- Cleans and transforms raw financial data
- Stores analytical datasets in SQLite
- Performs exploratory and performance analytics
- Computes advanced risk metrics
- Generates fund recommendations
- Visualizes insights through an interactive Power BI dashboard

The project follows a complete Data Analytics lifecycle from ETL to Business Intelligence.

---

## Objectives

- Build an automated ETL pipeline for mutual fund datasets
- Design an analytics-ready SQLite database
- Analyze fund performance and investor trends
- Compute risk-adjusted return metrics
- Develop an interactive Power BI dashboard
- Generate actionable investment insights

---

## Project Architecture

Raw CSV Data
↓
ETL Pipeline (Python + Pandas)
↓
Data Cleaning & Validation
↓
SQLite Database
↓
Analytics & Risk Models
↓
Power BI Dashboard
↓
Business Insights & Reporting

---

## 📂 Project Structure

MutualFundsAnalytics/

├── data/
│ ├── raw/
│ ├── processed/
│ └── db/
│
├── notebooks/
│ ├── 01_data_ingestion.ipynb
│ ├── 02_data_cleaning.ipynb
│ ├── 03_eda_analysis.ipynb
│ ├── 04_performance_analytics.ipynb
│ └── 05_advanced_analytics.ipynb
│
├── scripts/
│ ├── etl_pipeline.py
│ ├── live_nav_fetch.py
│ ├── compute_metrics.py
│ ├── recommender.py
│ └── run_pipeline.py
│
├── sql/
│ ├── schema.sql
│ └── queries.sql
│
├── dashboard/
│ └── bluestock_mf_dashboard.pbix
│
├── reports/
│ ├── Final_Report.pdf
│ └── Bluestock_MF_Presentation.pptx
│
└── README.md

---

## Datasets Used

| Dataset               | Description                    |
| --------------------- | ------------------------------ |
| Fund Master           | Mutual fund scheme metadata    |
| NAV History           | Daily NAV history for schemes  |
| AUM by Fund House     | Assets under management        |
| Monthly SIP Inflows   | SIP investment trends          |
| Category Inflows      | Category-wise fund flows       |
| Industry Folio Count  | Investor participation metrics |
| Scheme Performance    | Returns and risk statistics    |
| Investor Transactions | Investor transaction history   |
| Portfolio Holdings    | Sector allocation data         |
| Benchmark Indices     | Market benchmark performance   |

---

## Technologies Used

### Programming

* Python 3.11
* Pandas
* NumPy
* SciPy

### Database

* SQLite
* SQLAlchemy

### Analytics

* Jupyter Notebook
* Matplotlib
* Seaborn
* Plotly

### Business Intelligence

* Power BI

### Version Control

* Git
* GitHub

---

## ETL Pipeline

### Data Ingestion

- Loaded 10 mutual fund datasets
- Validated schema consistency
- Performed quality checks

### Data Cleaning

- Missing value handling
- Duplicate removal
- Data type standardization
- Date normalization

### Data Validation

- AMFI code validation
- NAV consistency checks
- Transaction quality checks

---

## Exploratory Data Analysis

Key analyses performed:

- NAV trend analysis (2022–2026)
- AUM growth analysis
- SIP inflow trends
- Category inflow heatmaps
- Investor demographics
- Geographic investment patterns
- Folio growth analysis
- Correlation analysis across schemes
- Sector allocation insights

---

## Performance Analytics

Metrics computed:

- Daily Returns
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Maximum Drawdown
- Tracking Error
- Composite Fund Scorecard

---

## Advanced Risk Analytics

### Value at Risk (VaR)

95% Historical VaR calculated for all schemes.

### Conditional VaR (CVaR)

Expected loss beyond the VaR threshold.

### Rolling Sharpe Ratio

90-day rolling risk-adjusted performance analysis.

### Portfolio Concentration

Herfindahl-Hirschman Index (HHI) based concentration measurement.

---

## Fund Recommendation Engine

A rule-based recommendation system that suggests mutual funds based on:

 Risk Appetite

  - Low
  - Moderate
  - High

Recommendations are ranked using Sharpe Ratio and risk profile compatibility.

---

## Interactive Dashboard

The Power BI dashboard contains four pages:

### 1. Industry Overview

- Industry KPIs
- AUM Trends
- AMC Comparison

### 2. Fund Performance

- Risk vs Return Analysis
- Fund Scorecard
- Benchmark Comparison

### 3. Investor Analytics

- Geographic Analysis
- Demographics
- Transaction Trends

### 4. SIP & Market Trends

- SIP Growth
- Category Inflows
- Market Correlation

### Link:
https://app.powerbi.com/groups/me/insights/93dea50f-713f-4a85-bf32-f1caf16de312?insightsSource=Desktop&experience=power-bi

---

## Key Findings

- SIP inflows reached record highs by the end of the study period.
- Industry folio count nearly doubled during the analysis period.
- Several schemes demonstrated superior risk-adjusted returns through Sharpe and Sortino analysis.
- Equity-oriented funds dominated category inflows.
- Investor participation was concentrated in major urban regions.
- Portfolio concentration varied significantly across schemes.

---

## Setup Instructions

### Clone Repository

git clone YOUR_REPOSITORY_URL

### Install Dependencies

pip install -r requirements.txt

### Run ETL Pipeline

python scripts/run_pipeline.py

### Launch Jupyter Notebooks

jupyter notebook

### Open Dashboard

Open:

dashboard/bluestock_mf_dashboard.pbix

using Power BI Desktop.

---

## Future Enhancements

- Real-time NAV ingestion
- Streamlit deployment
- Portfolio optimization engine
- Machine Learning based fund recommendation
- Automated report generation
- Cloud database integration

---

## Author

Asmita Gogate
B.Tech Artificial Intelligence
COEP Technological University, Pune
Intern at Bluestock Fintech

---

## Project Highlights

✔ End-to-End Data Analytics Project

✔ Data Engineering + ETL Pipeline

✔ Financial Performance Analytics

✔ Risk Modelling & VaR Analysis

✔ Interactive Power BI Dashboard

✔ SQL Database Design

✔ Business Intelligence Reporting

✔ Investment Recommendation System