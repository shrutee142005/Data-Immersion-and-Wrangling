import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(input_file)

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\n========== EXPLORATORY DATA ANALYSIS ==========")

# 1. Overall statistics
print("\n--- OVERALL SALES STATISTICS ---")

print("Total Revenue:", df["Total_Sales"].sum())
print("Total Quantity Sold:", df["Quantity"].sum())
print("Average Order Value:", df["Total_Sales"].mean())
print("Number of Records:", len(df))

# 2. Category analysis
print("\n--- SALES BY CATEGORY ---")

category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(
    ascending=False
)

print(category_sales)

# 3. Product analysis
print("\n--- SALES BY PRODUCT ---")

product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(
    ascending=False
)

print(product_sales)

# 4. City analysis
print("\n--- SALES BY CITY ---")

city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(
    ascending=False
)

print(city_sales)

# 5. Monthly sales
print("\n--- MONTHLY SALES ---")

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print(monthly_sales)

# 6. Gender analysis
print("\n--- SALES BY GENDER ---")

gender_sales = df.groupby("Gender")["Total_Sales"].sum()

print(gender_sales)

# 7. Age group analysis
print("\n--- SALES BY AGE GROUP ---")

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

age_sales = df.groupby("Age_Group", observed=False)["Total_Sales"].sum()

print(age_sales)

# Chart 1: Category Sales
plt.figure(figsize=(9, 5))
category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(output_dir / "category_sales.png")
plt.close()


# Chart 2: Product Sales
plt.figure(figsize=(9, 5))
product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(output_dir / "product_sales.png")
plt.close()


# Chart 3: City Sales
plt.figure(figsize=(9, 5))
city_sales.plot(kind="bar")

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(output_dir / "city_sales.png")
plt.close()


# Chart 4: Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig(output_dir / "monthly_sales_trend.png")
plt.close()


print("\n--- EDA COMPLETE ---")
print("Charts saved inside:", output_dir)