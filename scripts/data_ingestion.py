import pandas as pd
import os

data_folder = "../data/raw"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files")

for file in csv_files:

    print("\n" + "="*60)
    print("FILE:", file)

    df = pd.read_csv(os.path.join(data_folder, file))

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())