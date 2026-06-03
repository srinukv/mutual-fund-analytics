-- Dimension Table: Funds

CREATE TABLE dim_fund (

    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER UNIQUE,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    fund_manager TEXT,

    risk_category TEXT

);

--------------------------------------------------

-- Dimension Table: Date

CREATE TABLE dim_date (

    date_key INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE UNIQUE,

    year INTEGER,

    quarter INTEGER,

    month INTEGER,

    month_name TEXT

);

--------------------------------------------------

-- Fact Table: NAV

CREATE TABLE fact_nav (

    nav_key INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    date_key INTEGER,

    nav REAL,

    FOREIGN KEY(fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)

);

--------------------------------------------------

-- Fact Table: Transactions

CREATE TABLE fact_transactions (

    transaction_key INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    date_key INTEGER,

    investor_id TEXT,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    kyc_status TEXT,

    FOREIGN KEY(fund_key)
        REFERENCES dim_fund(fund_key),

    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)

);

--------------------------------------------------

-- Fact Table: Performance

CREATE TABLE fact_performance (

    performance_key INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_key INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    expense_ratio_pct REAL,

    aum_crore REAL,

    FOREIGN KEY(fund_key)
        REFERENCES dim_fund(fund_key)

);

--------------------------------------------------

-- Fact Table: AUM

CREATE TABLE fact_aum (

    aum_key INTEGER PRIMARY KEY AUTOINCREMENT,

    date_key INTEGER,

    fund_house TEXT,

    aum_crore REAL,

    num_schemes INTEGER,

    FOREIGN KEY(date_key)
        REFERENCES dim_date(date_key)

);