import pandas as pd
import os
from sqlalchemy import create_engine

# Database connection

engine = create_engine(
    "sqlite:///../bluestock_mf.db"
)

# Processed data folder

processed_path = "../data/processed"

# Files to load

files = [

    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"

]

for file in files:

    file_path = os.path.join(
        processed_path,
        file
    )

    df = pd.read_csv(file_path)

    table_name = (
        file
        .replace(".csv","")
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table_name} : {len(df)} rows"
    )

print(
    "\nAll datasets loaded successfully!"
)