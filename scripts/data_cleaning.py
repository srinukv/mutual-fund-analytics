import pandas as pd
import os

RAW_PATH = "../data/raw"
PROCESSED_PATH = "../data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)
def clean_nav_history():

    print("Cleaning NAV History...")

    df = pd.read_csv(
        f"{RAW_PATH}/02_nav_history.csv"
    )

    # convert date

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # sort

    df = df.sort_values(
        ["amfi_code","date"]
    )

    # remove duplicates

    df = df.drop_duplicates(
        subset=["amfi_code","date"]
    )

    # forward fill nav

    df["nav"] = (
        df.groupby("amfi_code")
        ["nav"]
        .ffill()
    )

    # nav > 0

    df = df[df["nav"] > 0]

    df.to_csv(
        f"{PROCESSED_PATH}/02_nav_history.csv",
        index=False
    )

    print("NAV cleaned")
def clean_transactions():

    print("Cleaning Transactions...")

    df = pd.read_csv(
        f"{RAW_PATH}/08_investor_transactions.csv"
    )

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    mapping = {

        "sip":"SIP",

        "lumpsum":"Lumpsum",

        "redemption":"Redemption"

    }

    df["transaction_type"] = (
        df["transaction_type"]
        .astype(str)
        .str.lower()
        .map(mapping)
        .fillna(
            df["transaction_type"]
        )
    )

    df = df[
        df["amount_inr"] > 0
    ]

    allowed = [
        "Verified",
        "Pending",
        "Rejected"
    ]

    invalid_kyc = df[
        ~df["kyc_status"]
        .isin(allowed)
    ]

    print(
        "Invalid KYC:",
        len(invalid_kyc)
    )

    df.to_csv(
        f"{PROCESSED_PATH}/08_investor_transactions.csv",
        index=False
    )

    print("Transactions cleaned")
def clean_performance():

    print("Cleaning Performance...")

    df = pd.read_csv(
        f"{RAW_PATH}/07_scheme_performance.csv"
    )

    returns_cols = [

        "return_1yr_pct",

        "return_3yr_pct",

        "return_5yr_pct"

    ]

    for col in returns_cols:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    anomalies = df[
        (df["return_1yr_pct"] > 100)
        |
        (df["return_1yr_pct"] < -50)
    ]

    anomalies.to_csv(
        f"{PROCESSED_PATH}/performance_anomalies.csv",
        index=False
    )

    invalid_expense = df[
        (df["expense_ratio_pct"] < 0.1)
        |
        (df["expense_ratio_pct"] > 2.5)
    ]

    print(
        "Invalid Expense Ratio:",
        len(invalid_expense)
    )

    df.to_csv(
        f"{PROCESSED_PATH}/07_scheme_performance.csv",
        index=False
    )

    print("Performance cleaned")
def clean_generic(file_name):

    df = pd.read_csv(
        f"{RAW_PATH}/{file_name}"
    )

    df = df.drop_duplicates()

    df = df.dropna(
        how="all"
    )

    df.to_csv(
        f"{PROCESSED_PATH}/{file_name}",
        index=False
    )

    print(file_name,"cleaned")
clean_nav_history()

clean_transactions()

clean_performance()

remaining = [

"01_fund_master.csv",

"03_aum_by_fund_house.csv",

"04_monthly_sip_inflows.csv",

"05_category_inflows.csv",

"06_industry_folio_count.csv",

"09_portfolio_holdings.csv",

"10_benchmark_indices.csv"

]

for file in remaining:

    clean_generic(file)

print("\nAll datasets cleaned.")