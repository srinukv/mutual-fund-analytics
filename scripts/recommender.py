import pandas as pd

# Load scheme performance data
df = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("\nRisk Appetite Options:")
print("1. Low")
print("2. Moderate")
print("3. High")

choice = input("\nEnter risk appetite: ").strip().lower()

# Map user choice to dataset risk grades
risk_mapping = {
    "low": ["Low"],
    "moderate": ["Moderate", "Moderately High"],
    "high": ["High", "Very High"]
}

if choice not in risk_mapping:
    print("Invalid choice!")
    exit()

# Filter matching funds
filtered_df = df[
    df["risk_grade"].isin(risk_mapping[choice])
]

# Select top 3 by Sharpe Ratio
top_funds = (
    filtered_df
    .sort_values("sharpe_ratio", ascending=False)
    .head(3)
)

print("\nTop Recommended Funds:\n")

print(
    top_funds[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "aum_crore"
        ]
    ]
)