SELECT
    scheme_name,
    aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    substr(date,1,7) AS month,
    AVG(nav) AS avg_nav
FROM 02_nav_history
GROUP BY month
ORDER BY month;

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM 04_monthly_sip_inflows
ORDER BY month;

SELECT
    state,
    COUNT(*) AS transactions,
    SUM(amount_inr) AS total_amount
FROM 08_investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

SELECT
    scheme_name,
    expense_ratio_pct
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1;

SELECT
    scheme_name,
    return_1yr_pct
FROM 07_scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

SELECT
    category,
    AVG(return_1yr_pct) AS avg_return
FROM 07_scheme_performance
GROUP BY category
ORDER BY avg_return DESC;

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM 03_aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;

SELECT
    city,
    COUNT(*) AS transaction_count
FROM 08_investor_transactions
GROUP BY city
ORDER BY transaction_count DESC
LIMIT 10;

SELECT
    sector,
    AVG(weight_pct) AS avg_weight
FROM 09_portfolio_holdings
GROUP BY sector
ORDER BY avg_weight DESC;