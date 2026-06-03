import pandas as pd
import os

raw_path = "../data/raw"

for file in os.listdir(raw_path):

    if file.endswith(".csv"):

        print("\n" + "="*50)
        print("FILE:", file)

        df = pd.read_csv(
            os.path.join(raw_path,file)
        )

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nShape:")
        print(df.shape)

        print("\nSample:")
        print(df.head())