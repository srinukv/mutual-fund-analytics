import pandas as pd

# Load datasets
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

# Unique AMFI codes
master_codes = set(
    fund_master["amfi_code"]
)

nav_codes = set(
    nav_history["amfi_code"]
)

# Find missing codes
missing_codes = master_codes - nav_codes

print("\nTotal Fund Master Codes:",
      len(master_codes))

print("Total NAV History Codes:",
      len(nav_codes))

print("Missing Codes:",
      len(missing_codes))

print("\nMissing Code List:")
print(missing_codes)