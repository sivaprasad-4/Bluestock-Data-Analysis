import os
import pandas as pd

folder_path = "data/raw"
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]
print(f"found {len(csv_files)} CSV files.\n")

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    print("=" * 60)
    print(f"Dataset: {file}")

    df = pd.read_csv(file_path, sep="\t")

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("=" * 60)
    print()
