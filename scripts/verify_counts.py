import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///../bluestock_mf.db"
)

tables = [

    "01_fund_master",
    "02_nav_history",
    "03_aum_by_fund_house",
    "04_monthly_sip_inflows",
    "05_category_inflows",
    "06_industry_folio_count",
    "07_scheme_performance",
    "08_investor_transactions",
    "09_portfolio_holdings",
    "10_benchmark_indices"

]

for table in tables:

    query = f"""
    SELECT COUNT(*) as count
    FROM "{table}"
    """

    count = pd.read_sql(
        query,
        engine
    )

    print(
        table,
        ":",
        count.iloc[0,0]
    )