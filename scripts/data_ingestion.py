import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

data_folder = BASE_DIR / "data" / "raw"

csv_files = [
    f.name
    for f in data_folder.glob("*.csv")
]

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "=" * 60)
    print("FILE:", file)

    df = pd.read_csv(data_folder / file)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())