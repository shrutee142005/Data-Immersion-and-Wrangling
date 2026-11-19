import pandas as pd

df = pd.read_excel(r"D:\Data-Immersion-warngling\data\raw\ApexPlanet_DataAnalytics_Dataset.xlsx")

# 1. Duplicate Order IDs
print("\n--- DUPLICATE ORDER IDs ---")
print(df["Order_ID"].duplicated().sum())

# 2. Invalid dates
print("\n--- INVALID DATES ---")
dates = pd.to_datetime(df["Order_Date"], errors="coerce")
print(dates.isna().sum())

# 3. Age validation
print("\n--- INVALID AGES ---")
print(df[(df["Age"] < 0) | (df["Age"] > 100)])

# 4. Quantity validation
print("\n--- INVALID QUANTITY ---")
print(df[df["Quantity"] <= 0])

# 5. Unit price validation
print("\n--- INVALID UNIT PRICE ---")
print(df[df["Unit_Price"] <= 0])

# 6. Sales calculation validation
print("\n--- SALES CALCULATION MISMATCH ---")
expected_sales = df["Quantity"] * df["Unit_Price"]

mismatch = ~(
    (df["Total_Sales"] - expected_sales).abs() < 0.01
)

print(df[mismatch])

# 7. Unique categories
print("\n--- CATEGORY VALUES ---")
print(df["Category"].unique())

# 8. Unique genders
print("\n--- GENDER VALUES ---")
print(df["Gender"].unique())

# 9. Unique cities
print("\n--- CITY VALUES ---")
print(df["City"].unique())

# 10. Unique products
print("\n--- PRODUCT VALUES ---")
print(df["Product"].unique())

# 11. Whitespace check
print("\n--- EXTRA WHITESPACE ---")

for col in df.select_dtypes(include="object").columns:
    count = df[col].str.strip().ne(df[col]).sum()
    if count > 0:
        print(col, ":", count)

# Investigate duplicate Order IDs
print("\n--- DUPLICATE ORDER ID RECORDS ---")

duplicate_orders = df[
    df["Order_ID"].duplicated(keep=False)
].sort_values("Order_ID")

print(duplicate_orders.to_string(index=False))

print("\n--- DUPLICATE ID FREQUENCY ---")
print(df["Order_ID"].value_counts()[lambda x: x > 1])

print("\n--- ORDER ID INVESTIGATION ---")

order_id = "ORD100050"

records = df[df["Order_ID"] == order_id]

print("Total records:", len(records))
print("Unique customers:", records["Customer_ID"].nunique())
print("Unique dates:", records["Order_Date"].nunique())
print("Unique products:", records["Product"].nunique())

print("\nFull records:")
print(records[
    ["Order_ID", "Order_Date", "Customer_ID", "Product", "Quantity", "Total_Sales"]
].to_string(index=False))

# Check all duplicate Order IDs
print("\n--- ALL DUPLICATE ORDER IDs ---")

duplicate_ids = df[df["Order_ID"].duplicated(keep=False)]

print(
    duplicate_ids.groupby("Order_ID").size()
    .sort_values(ascending=False)
)

print("\nTotal affected records:", len(duplicate_ids))
print("Unique affected Order IDs:", duplicate_ids["Order_ID"].nunique())

# Missing values investigation

print("\n--- MISSING AGE RECORDS ---")

print(df[df["Age"].isnull()][
    ["Customer_ID", "Customer_Name", "Gender", "City", "Age"]
].to_string(index=False))


print("\n--- AGE STATISTICS ---")

print(df["Age"].describe())


print("\n--- AGE BY GENDER ---")

print(df.groupby("Gender")["Age"].median())


print("\n--- MISSING CITY RECORDS ---")

print(df[df["City"].isnull()][
    ["Customer_ID", "Customer_Name", "Age", "Gender", "City"]
].to_string(index=False))


print("\n--- CITY FREQUENCY ---")

print(df["City"].value_counts())