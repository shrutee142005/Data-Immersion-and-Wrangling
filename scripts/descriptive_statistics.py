
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports"

output_dir.mkdir(parents=True, exist_ok=True)

# Load cleaned dataset
df = pd.read_csv(input_file)

print("\n========== DESCRIPTIVE STATISTICS ==========")

# 1. Dataset overview
print("\n--- DATASET OVERVIEW ---")
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("\nColumn Names:")
print(df.columns.tolist())

# 2. Numerical statistics
print("\n--- NUMERICAL STATISTICS ---")

numerical_stats = df.describe()

print(numerical_stats)

# 3. Categorical statistics
print("\n--- CATEGORICAL STATISTICS ---")

categorical_stats = df.describe(include="object")

print(categorical_stats)

# 4. Missing values
print("\n--- MISSING VALUES ---")

missing_values = df.isnull().sum()

print(missing_values)

# 5. Unique values
print("\n--- UNIQUE VALUES ---")

for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")

# 6. Sales-specific statistics
print("\n--- SALES STATISTICS ---")

print("Minimum Sales:", df["Total_Sales"].min())
print("Maximum Sales:", df["Total_Sales"].max())
print("Median Sales:", df["Total_Sales"].median())
print("Standard Deviation:", df["Total_Sales"].std())

# 7. Quantity statistics
print("\n--- QUANTITY STATISTICS ---")

print("Minimum Quantity:", df["Quantity"].min())
print("Maximum Quantity:", df["Quantity"].max())
print("Average Quantity:", df["Quantity"].mean())
print("Median Quantity:", df["Quantity"].median())

# Save numerical statistics
numerical_stats.to_csv(output_dir / "numerical_statistics.csv")

# Save categorical statistics
categorical_stats.to_csv(output_dir / "categorical_statistics.csv")

print("\nStatistics reports saved successfully!")
print("Location:", output_dir)
