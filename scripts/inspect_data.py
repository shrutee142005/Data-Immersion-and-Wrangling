import pandas as pd
from pathlib import Path

# Dataset path
file_path = Path(r"D:\Data-Immersion-warngling\data\raw\ApexPlanet_DataAnalytics_Dataset.xlsx")

# Load dataset
df = pd.read_excel(file_path)

# Basic dataset information
print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- DATASET INFO ---")
df.info()