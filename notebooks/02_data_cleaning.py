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

# validate customer data
print("\nValidating customer data")

#check missing customer_id
print("\nMissing customer IDs:",
      df["customer_id"].isnull().sum())

#check missing customer identities
print("\nMissing customer identities:",
      df["customer_unique_id"].isnull().sum())

# Check invalid state codes
valid_states = {
    "AC", "AL", "AP", "AM", "BA", "CE", "DF",
    "ES", "GO", "MA", "MT", "MS", "MG", "PA",
    "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
    "RO", "RR", "SC", "SP", "SE", "TO"
}

invalid_states = set(df["customer_state"].dropna().unique()) - valid_states

print("Unexpected state codes:", invalid_states)

# Check duplicate customer IDs
print(
    "Duplicate customer IDs:",
    df["customer_id"].duplicated().sum()
)

# Save cleaned dataset locally
cleaned_dir = project_dir / "data" / "processed"
cleaned_dir.mkdir(parents=True, exist_ok=True)

cleaned_file = cleaned_dir / "olist_customers_cleaned.csv"
df.to_csv(cleaned_file, index=False)

print("\nCleaned dataset saved to:", cleaned_file)
print("Final dataset shape:", df.shape)
