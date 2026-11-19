import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

file_path = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"

df = pd.read_csv(file_path)

print("\n--- FINAL VALIDATION ---")

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAge Imputation Count:")
print(df["Age_Imputed"].sum())

print("\nCity Missing Count:")
print(df["City_Missing_Flag"].sum())

print("\nDuplicate Order ID Flags:")
print(df["Duplicate_Order_ID_Flag"].sum())

print("\nSales Mismatch Flags:")
print(df["Sales_Mismatch_Flag"].sum())

print("\nCities after cleaning:")
print(df["City"].value_counts())

print("\nAge Statistics:")
print(df["Age"].describe())

print("\nDate Data Type:")
print(df["Order_Date"].dtype)

print("\nFirst 5 Cleaned Records:")
print(df.head())