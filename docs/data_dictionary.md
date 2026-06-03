# Mutual Fund Analytics Data Dictionary

## Project Overview

This project analyzes Indian Mutual Fund industry data using Python, Pandas, SQLite, and SQLAlchemy. The datasets contain information about mutual fund schemes, NAV history, AUM, SIP inflows, investor transactions, portfolio holdings, and benchmark indices.

Source References:

* AMFI (Association of Mutual Funds in India)
* MFAPI NAV Data
* Simulated Investor and Portfolio Datasets

---

# 01_fund_master

**Description:** Master dataset containing details of mutual fund schemes.

| Column             | Data Type | Description                                           |
| ------------------ | --------- | ----------------------------------------------------- |
| amfi_code          | INTEGER   | Unique mutual fund scheme identifier assigned by AMFI |
| fund_house         | TEXT      | Asset Management Company (AMC) name                   |
| scheme_name        | TEXT      | Name of the mutual fund scheme                        |
| category           | TEXT      | Primary scheme category                               |
| sub_category       | TEXT      | Detailed category classification                      |
| plan               | TEXT      | Direct or Regular plan                                |
| launch_date        | DATE      | Scheme launch date                                    |
| benchmark          | TEXT      | Benchmark index used for comparison                   |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage                       |
| exit_load_pct      | REAL      | Exit load charged on redemption                       |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount                         |
| min_lumpsum_amount | INTEGER   | Minimum lump sum investment amount                    |
| fund_manager       | TEXT      | Fund manager name                                     |
| risk_category      | TEXT      | Risk classification of scheme                         |
| sebi_category_code | TEXT      | SEBI category code                                    |

---

# 02_nav_history

**Description:** Historical daily NAV values for mutual fund schemes.

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Scheme identifier             |
| date      | DATE      | NAV date                      |
| nav       | REAL      | Net Asset Value of the scheme |

---

# 03_aum_by_fund_house

**Description:** Assets Under Management statistics by fund house.

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Fund house name           |
| aum_lakh_crore | REAL      | AUM in lakh crore rupees  |
| aum_crore      | REAL      | AUM in crore rupees       |
| num_schemes    | INTEGER   | Number of schemes managed |

---

# 04_monthly_sip_inflows

**Description:** Monthly SIP investment statistics.

| Column                    | Data Type | Description                           |
| ------------------------- | --------- | ------------------------------------- |
| month                     | TEXT      | Reporting month                       |
| sip_inflow_crore          | REAL      | SIP inflows in crore rupees           |
| active_sip_accounts_crore | REAL      | Active SIP accounts in crore          |
| new_sip_accounts_lakh     | REAL      | Newly registered SIP accounts in lakh |
| sip_aum_lakh_crore        | REAL      | SIP assets under management           |
| yoy_growth_pct            | REAL      | Year-over-year growth percentage      |

---

# 05_category_inflows

**Description:** Net inflows by mutual fund category.

| Column           | Data Type | Description                       |
| ---------------- | --------- | --------------------------------- |
| month            | TEXT      | Reporting month                   |
| category         | TEXT      | Fund category                     |
| net_inflow_crore | REAL      | Net inflow amount in crore rupees |

---

# 06_industry_folio_count

**Description:** Industry folio statistics.

| Column              | Data Type | Description            |
| ------------------- | --------- | ---------------------- |
| month               | TEXT      | Reporting month        |
| total_folios_crore  | REAL      | Total folios in crore  |
| equity_folios_crore | REAL      | Equity folios in crore |
| debt_folios_crore   | REAL      | Debt folios in crore   |
| hybrid_folios_crore | REAL      | Hybrid folios in crore |
| others_folios_crore | REAL      | Other folios in crore  |

---

# 07_scheme_performance

**Description:** Risk and performance metrics for mutual fund schemes.

| Column             | Data Type | Description                             |
| ------------------ | --------- | --------------------------------------- |
| amfi_code          | INTEGER   | Scheme identifier                       |
| scheme_name        | TEXT      | Scheme name                             |
| fund_house         | TEXT      | Fund house name                         |
| category           | TEXT      | Fund category                           |
| plan               | TEXT      | Scheme plan type                        |
| return_1yr_pct     | REAL      | One-year return percentage              |
| return_3yr_pct     | REAL      | Three-year annualized return percentage |
| return_5yr_pct     | REAL      | Five-year annualized return percentage  |
| benchmark_3yr_pct  | REAL      | Benchmark three-year return             |
| alpha              | REAL      | Alpha performance metric                |
| beta               | REAL      | Beta risk metric                        |
| sharpe_ratio       | REAL      | Sharpe ratio                            |
| sortino_ratio      | REAL      | Sortino ratio                           |
| std_dev_ann_pct    | REAL      | Annualized standard deviation           |
| max_drawdown_pct   | REAL      | Maximum drawdown percentage             |
| aum_crore          | REAL      | Assets under management in crore rupees |
| expense_ratio_pct  | REAL      | Expense ratio percentage                |
| morningstar_rating | INTEGER   | Morningstar rating                      |
| risk_grade         | TEXT      | Risk grade classification               |

---

# 08_investor_transactions

**Description:** Individual investor transaction records.

| Column             | Data Type | Description                  |
| ------------------ | --------- | ---------------------------- |
| investor_id        | TEXT      | Unique investor identifier   |
| transaction_date   | DATE      | Transaction date             |
| amfi_code          | INTEGER   | Mutual fund scheme code      |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption  |
| amount_inr         | REAL      | Transaction amount in INR    |
| state              | TEXT      | Investor state               |
| city               | TEXT      | Investor city                |
| city_tier          | TEXT      | City classification tier     |
| age_group          | TEXT      | Investor age group           |
| gender             | TEXT      | Investor gender              |
| annual_income_lakh | REAL      | Annual income in lakh rupees |
| payment_mode       | TEXT      | Mode of payment              |
| kyc_status         | TEXT      | KYC verification status      |

---

# 09_portfolio_holdings

**Description:** Portfolio holdings of mutual fund schemes.

| Column            | Data Type | Description                  |
| ----------------- | --------- | ---------------------------- |
| amfi_code         | INTEGER   | Scheme identifier            |
| stock_symbol      | TEXT      | Stock market symbol          |
| stock_name        | TEXT      | Company name                 |
| sector            | TEXT      | Industry sector              |
| weight_pct        | REAL      | Portfolio weight percentage  |
| market_value_cr   | REAL      | Market value in crore rupees |
| current_price_inr | REAL      | Current stock price in INR   |
| portfolio_date    | DATE      | Portfolio disclosure date    |

---

# 10_benchmark_indices

**Description:** Historical benchmark index values.

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Index closing value  |

---

# Data Quality Checks Performed

1. Removed duplicate records.
2. Standardized date formats.
3. Validated NAV values greater than zero.
4. Standardized transaction types.
5. Validated transaction amounts greater than zero.
6. Checked KYC status values.
7. Validated performance metrics as numeric.
8. Checked expense ratio ranges.
9. Verified database row counts after loading.
10. Generated anomaly report for performance metrics.

---

# Database Information

Database Name: bluestock_mf.db

Technology Stack:

* Python
* Pandas
* SQLite
* SQLAlchemy

Project Deliverables:

* 10 Cleaned CSV Files
* SQLite Database
* SQL Schema
* Analytical Queries
* Data Dictionary
