from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent
file_path= project_dir/"data"/"olist_customers_dataset.csv"

df = pd.read_csv(file_path)

print("Fisrt 5 rows of the dataset:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset columns:")
print(df.columns)

print("\nDataset info:")
print(df.info())

print("\nDataset description:")
print(df.describe())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nUnique values in each column:")
for column in df.columns:
    unique_values = df[column].nunique()
    print(f"{column}: {unique_values} unique values")

print("\nDuplicate rows in the dataset:")
print(df.duplicated().sum())

print("\nCustomers by state:")
print(df['customer_state'].value_counts().head)

# Customer distribution by state
print("\nTop 10 states with the most customers:")
state_counts = df['customer_state'].value_counts().head(10)
print(state_counts)

#Customer distribution by city
print("\nTop 10 cities with the most customers:")
city_counts = df['customer_city'].value_counts().head(10)
print(city_counts)

# Save the results in reports folder
reports_dir = project_dir/"reports"
if not reports_dir.exists():
    reports_dir.mkdir()

# Save the state counts to a CSV file
state_counts.to_csv(reports_dir/"customer_distribution_by_state.csv", index=True)

# Save the city counts to a CSV file
city_counts.to_csv(reports_dir/"customer_distribution_by_city.csv", index=True)

print("\nAnalysis completed. The results have been saved in the 'reports' folder.")


# Data quality analysis
print("\nData Quality Analysis:")

# 1. Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 2. Check for duplicate rows

# 2. Check for duplicate rows using smaller chunks
print("\nDuplicate rows in the dataset:")

chunk_size = 10000
seen_rows = set()
duplicate_count = 0

for start in range(0, len(df), chunk_size):
    chunk = df.iloc[start:start + chunk_size]

    for row in chunk.itertuples(index=False, name=None):
        if row in seen_rows:
            duplicate_count += 1
        else:
            seen_rows.add(row)

print("Duplicate rows:", duplicate_count)

# 3. Check duplicate customer IDs
print("\nDuplicate customer IDs:")
print(df["customer_id"].duplicated().sum())

# 4. Check unique customer IDs
print("\nUnique customer IDs:")
print(df["customer_id"].nunique())

print("\nUnique customer identities:")
print(df["customer_unique_id"].nunique())

# 5. Check blank text values
print("\nBlank values in text columns:")
for column in ["customer_city", "customer_state"]:
    blank_count = (
        df[column].astype("string").str.strip().eq("").sum()
    )
    print(f"{column}: {blank_count} blank values")

# 6. Check state values
print("\nStates present in the dataset:")
print(sorted(df["customer_state"].dropna().unique()))

# 7. Create a quality summary report
quality_reports = pd.DataFrame({
    "check": [
        "Total rows",
        "Total columns",
        "Total missing values",
        "Duplicate rows",
        "Duplicate customer IDs",
        "Unique customer IDs",
        "Unique customer identities"
    ],
    "result": [
        len(df),
        len(df.columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum()),
        int(df["customer_id"].duplicated().sum()),
        int(df["customer_id"].nunique()),
        int(df["customer_unique_id"].nunique())
    ]
})

reports_dir = project_dir / "reports"
reports_dir.mkdir(exist_ok=True)

quality_reports.to_csv(
    reports_dir / "data_quality_summary.csv",
    index=False
)

print(
    "\nQuality summary report saved as "
    "'data_quality_summary.csv' in the 'reports' folder."
)
