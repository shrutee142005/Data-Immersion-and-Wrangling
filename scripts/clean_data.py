import pandas as pd
from pathlib import Path

# Project directory
BASE_DIR = Path(__file__).resolve().parents[1]

# File paths
input_file = BASE_DIR / "data" / "raw" / "ApexPlanet_DataAnalytics_Dataset.xlsx"
output_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"

# Load original dataset
df = pd.read_excel(input_file)

print("Original dataset shape:", df.shape)

# 1. Standardize text columns
text_columns = df.select_dtypes(include="str").columns

for col in text_columns:
    df[col] = df[col].str.strip()

# 2. Convert Order_Date into datetime
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

# 3. Handle missing Age using gender-wise median
df["Age_Imputed"] = df["Age"].isna()

df["Age"] = df.groupby("Gender")["Age"].transform(
    lambda x: x.fillna(x.median())
)

# 4. Handle missing City
df["City_Missing_Flag"] = df["City"].isna()

df["City"] = df["City"].fillna("Unknown")

# 5. Flag duplicate Order IDs
df["Duplicate_Order_ID_Flag"] = df["Order_ID"].duplicated(
    keep=False
)

# 6. Validate sales calculation
expected_sales = df["Quantity"] * df["Unit_Price"]

df["Sales_Mismatch_Flag"] = (
    (df["Total_Sales"] - expected_sales).abs() > 0.01
)

# 7. Save cleaned dataset
output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False)

# 8. Cleaning summary
print("\n--- CLEANING SUMMARY ---")

print("Final shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate Order ID records flagged:")
print(df["Duplicate_Order_ID_Flag"].sum())

print("\nAge values imputed:")
print(df["Age_Imputed"].sum())

print("\nCity values replaced:")
print(df["City_Missing_Flag"].sum())

print("\nSales mismatches:")
print(df["Sales_Mismatch_Flag"].sum())

print("\nCleaned file saved at:")
print(output_file)