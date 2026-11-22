# SQL Business Analysis

## Project: Exploratory Data Analysis & Business Intelligence

**Database:** SQLite  
**Table Name:** sales  
**Dataset Size:** 1,000 Records

---

## 1. Which category generates the highest revenue?

### SQL Query

```sql
SELECT
    Category,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Category
ORDER BY Revenue DESC;
```

### Result

| Category | Revenue |
|---|---:|
| Electronics | 50,778,581.70 |
| Education | 25,031,689.40 |
| Grocery | 22,231,711.28 |
| Furniture | 21,521,561.48 |
| Fashion | 19,835,895.79 |

**Insight:** Electronics generates the highest revenue among all categories.

---

## 2. Which city generates the highest revenue?

### SQL Query

```sql
SELECT
    City,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;
```

### Result

| City | Revenue |
|---|---:|
| Patna | 19,285,966.89 |
| Kolkata | 18,884,349.57 |
| Bengaluru | 18,773,574.32 |
| Mumbai | 18,757,050.17 |
| Hyderabad | 17,166,766.87 |
| Delhi | 16,097,079.00 |
| Pune | 14,513,175.90 |
| Gaya | 14,380,859.39 |
| Unknown | 1,540,617.54 |

**Insight:** Patna is the highest revenue-generating city.

---

## 3. Which product generates the highest revenue?

### SQL Query

```sql
SELECT
    Product,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC;
```

### Result

| Product | Revenue |
|---|---:|
| Laptop | 25,443,008.51 |
| Mobile | 25,335,573.19 |
| Book | 25,031,689.40 |
| Rice | 22,231,711.28 |
| Chair | 21,521,561.48 |
| Shoes | 19,835,895.79 |

**Insight:** Laptop generates the highest revenue, closely followed by Mobile.

---

## 4. Which month generates the highest revenue?

### SQL Query

```sql
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    SUM(Total_Sales) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Revenue DESC;
```

### Result

| Month | Revenue |
|---|---:|
| 2025-03 | 13,059,899.94 |
| 2025-06 | 12,912,332.64 |
| 2025-11 | 12,627,620.22 |
| 2025-10 | 12,500,936.50 |
| 2025-12 | 12,299,904.44 |
| 2025-04 | 12,222,700.17 |
| 2025-07 | 11,746,226.80 |
| 2025-02 | 11,511,181.46 |
| 2025-05 | 10,984,689.25 |
| 2025-01 | 10,096,190.73 |
| 2025-08 | 9,448,471.22 |
| 2025-09 | 9,179,896.29 |
| 2026-01 | 809,389.99 |

**Insight:** March 2025 recorded the highest revenue. January 2026 appears to contain only partial-period data and should not be compared directly with full months without checking the date coverage.

---

## 5. Which gender contributes more to sales?

### SQL Query

```sql
SELECT
    Gender,
    SUM(Total_Sales) AS Revenue,
    AVG(Total_Sales) AS Average_Sales,
    COUNT(*) AS Total_Records
FROM sales
GROUP BY Gender
ORDER BY Revenue DESC;
```

### Result

| Gender | Revenue | Average Sales | Records |
|---|---:|---:|---:|
| Male | 72,463,550.63 | 141,807.34 | 511 |
| Female | 66,935,889.02 | 136,883.21 | 489 |

**Insight:** Male customers contribute slightly more total revenue and transaction records.

---

## 6. Which age group generates the highest revenue?

### SQL Query

```sql
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18-25'
        WHEN Age BETWEEN 26 AND 35 THEN '26-35'
        WHEN Age BETWEEN 36 AND 45 THEN '36-45'
        WHEN Age BETWEEN 46 AND 55 THEN '46-55'
        ELSE '56-65'
    END AS Age_Group,
    SUM(Total_Sales) AS Revenue,
    COUNT(*) AS Total_Records
FROM sales
GROUP BY Age_Group
ORDER BY Revenue DESC;
```

### Result

| Age Group | Revenue |
|---|---:|
| 36-45 | 31,533,245.71 |
| 26-35 | 29,632,336.96 |
| 46-55 | 28,216,508.63 |
| 56-65 | 27,733,251.41 |
| 18-25 | 22,284,096.94 |

**Insight:** The 36–45 age group contributes the highest revenue.

---

## 7. Which category has the highest average transaction value?

### SQL Query

```sql
SELECT
    Category,
    AVG(Total_Sales) AS Average_Sales,
    COUNT(*) AS Total_Transactions
FROM sales
GROUP BY Category
ORDER BY Average_Sales DESC;
```

### Result

| Category | Average Sales |
|---|---:|
| Grocery | 145,305.30 |
| Electronics | 143,442.32 |
| Education | 140,627.47 |
| Furniture | 135,355.73 |
| Fashion | 127,153.18 |

**Insight:** Grocery has the highest average transaction value, while Electronics generates the highest total revenue.

---

# SQL Concepts Demonstrated

| SQL Concept | Purpose |
|---|---|
| SELECT | Retrieve data |
| SUM() | Calculate total revenue |
| AVG() | Calculate average sales |
| COUNT() | Count records |
| GROUP BY | Group records by category |
| ORDER BY | Sort results |
| CASE | Create age groups |
| strftime() | Extract month from date |
| Aggregate Functions | Summarize business data |

# Conclusion

SQL analysis helped answer important business questions related to revenue, products, categories, customer demographics, cities, and monthly trends.

The queries demonstrate the practical application of SQL aggregation, grouping, filtering, sorting, and date analysis in business intelligence.
