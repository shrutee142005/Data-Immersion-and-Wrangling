import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

csv_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
db_file = BASE_DIR / "data" / "sales_analysis.db"

# Load dataset
df = pd.read_csv(csv_file)

# Create SQLite database
conn = sqlite3.connect(db_file)

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database created successfully!")
print("Total records:", len(df))

# Business Question 1
query = """
SELECT Category,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 1 ---")
print("Which category generates the highest revenue?")
print(result)

# Business Question 2
query = """
SELECT City,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 2 ---")
print("Which city generates the highest revenue?")
print(result)

# Business Question 3
query = """
SELECT Product,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 3 ---")
print("Which product generates the highest revenue?")
print(result)

# Business Question 4
query = """
SELECT strftime('%Y-%m', Order_Date) AS Month,
       SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 4 ---")
print("Which month generates the highest revenue?")
print(result)

# Business Question 5
query = """
SELECT Gender,
       SUM(Total_Sales) AS Revenue,
       AVG(Total_Sales) AS Average_Sales,
       COUNT(*) AS Total_Orders
FROM sales
GROUP BY Gender
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 5 ---")
print("Which gender contributes more revenue?")
print(result)

print(result.to_string(index=False))

# Business Question 6
query = """
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        WHEN Age BETWEEN 56 AND 65 THEN '56-65'
    END AS Age_Group,
    SUM(Total_Sales) AS Revenue,
    COUNT(*) AS Total_Records
FROM sales
GROUP BY Age_Group
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 6 ---")
print("Which age group generates the highest revenue?")
print(result.to_string(index=False))

# Business Question 7
query = """
SELECT Category,
       AVG(Total_Sales) AS Average_Transaction_Value,
       COUNT(*) AS Total_Orders
FROM sales
GROUP BY Category
ORDER BY Average_Transaction_Value DESC;
"""

result = pd.read_sql_query(query, conn)

print("\n--- BUSINESS QUESTION 7 ---")
print("Which category has the highest average transaction value?")
print(result.to_string(index=False))

conn.close()