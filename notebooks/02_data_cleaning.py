from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "olist_customers_dataset.csv"
print("Looking for dataset at:", file_path)
df = pd.read_csv(file_path)

#Check column names for extra spaces
df.columns = df.columns.str.strip()
#check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# check blank text values
for column in["customer_city", "customer_state"]:
    blank_count = df[column].astype("string").str.strip().eq("").sum()
    print(f"{column}: {blank_count} blank values")

# Check customer ID uniqueness
print("\nUnique customer IDs:", df["customer_id"].nunique())
print("Total records:", len(df))

# Standardize text spacing
for column in ["customer_city", "customer_state"]:
    df[column] = df[column].astype("string").str.strip()

print("\nDataset shape after basic cleaning checks:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())
