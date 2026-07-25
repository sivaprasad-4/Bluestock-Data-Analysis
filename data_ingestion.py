import os
import pandas as pd
from io import StringIO

folder_path = "data/raw"

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

print(f"Found {len(csv_files)} CSV files.\n")

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    print("=" * 60)
    print(f"Dataset: {file}")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().replace("\\t", "\t")

        df = pd.read_csv(StringIO(content), sep="\t")

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("=" * 60)
    print()