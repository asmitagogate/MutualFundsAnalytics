--Q1
SELECT fund_house,
       aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;
--Q2
SELECT strftime('%Y-%m', nav_date) month,
       AVG(nav) avg_nav
FROM fact_nav
GROUP BY month;
--Q3
SELECT *
FROM dim_fund
WHERE expense_ratio_pct < 1;
--Q4
SELECT state,
       COUNT(*) transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;
--Q5
SELECT transaction_type,
       SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type;
--Q6
SELECT scheme_name,
       sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;
--Q7
SELECT scheme_name,
       alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;
--Q8
SELECT risk_grade,
       COUNT(*)
FROM fact_performance
GROUP BY risk_grade;
--Q9
SELECT city_tier,
       SUM(amount_inr)
FROM fact_transactions
GROUP BY city_tier;
--Q10
SELECT fund_house,
       AVG(return_3yr_pct)
FROM fact_performance
GROUP BY fund_house
ORDER BY AVG(return_3yr_pct) DESC;
