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