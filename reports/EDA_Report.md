# Exploratory Data Analysis (EDA) & Business Intelligence Report

## 1. Project Overview

This project focuses on Exploratory Data Analysis (EDA) and Business Intelligence using a sales dataset. The objective is to identify meaningful patterns, trends, relationships, and business insights from sales data using Python, Pandas, Matplotlib, Seaborn, and SQL.

The analysis helps understand sales performance across categories, products, cities, customer demographics, and time periods.

## 2. Dataset Description

- Total Records: 1,000
- Total Columns: 16
- Dataset Type: Sales Transaction Data
- Data Source: Cleaned sales dataset from the previous Data Cleaning & Wrangling task.

The dataset includes order information, customer details, product categories, sales values, quantity, city, gender, age, and data quality flags.

## 3. Tools and Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- SQL
- Visual Studio Code
- GitHub

## 4. Descriptive Statistics

Descriptive statistics were calculated to understand the distribution and characteristics of numerical variables.

| Metric | Value |
|---|---:|
| Total Revenue | ₹139,399,439.65 |
| Total Records | 1,000 |
| Average Sales | ₹139,399.44 |
| Median Sales | ₹108,594.03 |
| Maximum Sales | ₹493,677.50 |
| Minimum Sales | ₹437.34 |
| Average Quantity | 5.435 |
| Average Customer Age | 41.34 years |

The sales data shows considerable variation between transactions. The mean sales value is higher than the median, indicating the presence of some high-value transactions.

## 5. Univariate Analysis

Univariate analysis was performed to examine individual numerical and categorical variables.

### Numerical Variables

Histograms were created for:

- Age
- Quantity
- Total Sales

These plots help understand distributions, frequency patterns, and variation in numerical data.

### Categorical Variables

Bar charts were created for:

- Category
- Product
- City
- Gender

### Key Findings

- Electronics is the most frequent category, with 354 records.
- Mobile is the most frequently purchased product, with 184 records.
- Patna has the highest number of records, with 135 transactions.
- Male customers account for 511 records.
- Female customers account for 489 records.

## 6. Business Analysis Using SQL

Seven business questions were answered using SQL queries involving GROUP BY, ORDER BY, SUM, AVG, COUNT, CASE, and date-based aggregation.

### Question 1: Which category generates the highest revenue?

| Category | Revenue |
|---|---:|
| Electronics | ₹50,778,581.70 |
| Education | ₹25,031,689.40 |
| Grocery | ₹22,231,711.28 |
| Furniture | ₹21,521,561.48 |
| Fashion | ₹19,835,895.79 |

**Insight:** Electronics is the highest revenue-generating category.

### Question 2: Which city generates the highest revenue?

| City | Revenue |
|---|---:|
| Patna | ₹19,285,966.89 |
| Kolkata | ₹18,884,349.57 |
| Bengaluru | ₹18,773,574.32 |
| Mumbai | ₹18,757,050.17 |
| Hyderabad | ₹17,166,766.87 |
| Delhi | ₹16,097,079.00 |
| Pune | ₹14,513,175.90 |
| Gaya | ₹14,380,859.39 |
| Unknown | ₹1,540,617.54 |

**Insight:** Patna generates the highest revenue among the cities in the dataset.

### Question 3: Which product generates the highest revenue?

| Product | Revenue |
|---|---:|
| Laptop | ₹25,443,008.51 |
| Mobile | ₹25,335,573.19 |
| Book | ₹25,031,689.40 |
| Rice | ₹22,231,711.28 |
| Chair | ₹21,521,561.48 |
| Shoes | ₹19,835,895.79 |

**Insight:** Laptop is the highest revenue-generating product, closely followed by Mobile.

### Question 4: Which month generates the highest revenue?

| Month | Revenue |
|---|---:|
| March 2025 | ₹13,059,899.94 |
| June 2025 | ₹12,912,332.64 |
| November 2025 | ₹12,627,620.22 |
| October 2025 | ₹12,500,936.50 |
| December 2025 | ₹12,299,904.44 |

**Insight:** March 2025 recorded the highest revenue in the analyzed period.

### Question 5: Which gender contributes more to sales?

| Gender | Revenue | Average Sales | Records |
|---|---:|---:|---:|
| Male | ₹72,463,550.63 | ₹141,807.34 | 511 |
| Female | ₹66,935,889.02 | ₹136,883.21 | 489 |

**Insight:** Male customers contribute slightly more revenue and transaction records than female customers.

### Question 6: Which age group generates the highest revenue?

| Age Group | Revenue |
|---|---:|
| 36–45 | ₹31,533,245.71 |
| 26–35 | ₹29,632,336.96 |
| 46–55 | ₹28,216,508.63 |
| 56–65 | ₹27,733,251.41 |
| 18–25 | ₹22,284,096.94 |

**Insight:** Customers aged 36–45 contribute the highest revenue.

### Question 7: Which category has the highest average transaction value?

| Category | Average Sales |
|---|---:|
| Grocery | ₹145,305.30 |
| Electronics | ₹143,442.32 |
| Education | ₹140,627.47 |
| Furniture | ₹135,355.73 |
| Fashion | ₹127,153.18 |

**Insight:** Grocery has the highest average transaction value, while Electronics generates the highest total revenue.

## 7. Multivariate Analysis and Correlation

Correlation analysis was performed on numerical variables to identify relationships between them.

| Variable Pair | Correlation |
|---|---:|
| Quantity vs Total Sales | 0.647 |
| Unit Price vs Total Sales | 0.686 |
| Age vs Total Sales | 0.001 |
| Age vs Quantity | -0.029 |

### Interpretation

- Unit Price has a moderately strong positive relationship with Total Sales.
- Quantity also shows a positive relationship with Total Sales.
- Age has almost no linear relationship with Total Sales.
- Higher quantities and higher unit prices are generally associated with increased sales values.

Correlation does not imply causation.

## 8. Scatter Plot Analysis

Scatter plots were created to analyze the relationship between:

- Age and Total Sales
- Quantity and Total Sales
- Unit Price and Total Sales

The plots help visualize the distribution of sales values and relationships between numerical variables.

## 9. Business Intelligence Dashboard

A static dashboard was created to summarize the important business metrics and insights.

### Key Performance Indicators (KPIs)

- Total Revenue: ₹139.40 Million
- Total Records: 1,000
- Average Sales: ₹139,399.44
- Top Category: Electronics

### Dashboard Visualizations

- Revenue by Category
- Monthly Sales Trend
- Revenue by Product
- Revenue by City

The dashboard provides a consolidated view of sales performance and helps stakeholders understand business trends quickly.

## 10. Key Business Recommendations

1. Increase marketing efforts for Electronics due to its high revenue contribution.
2. Promote laptops and mobiles through targeted campaigns.
3. Investigate sales opportunities in cities with comparatively lower revenue.
4. Focus marketing campaigns on the 36–45 age group.
5. Explore strategies to improve Fashion category revenue.
6. Use monthly sales trends to plan promotions and inventory.
7. Improve customer location data quality to reduce Unknown city records.

## 11. Conclusion

The Exploratory Data Analysis and Business Intelligence project successfully transformed sales data into meaningful business insights.

Using Python visualizations, descriptive statistics, SQL queries, correlation analysis, and a dashboard, the project identified the top-performing category, product, city, month, and customer segment.

The analysis demonstrates how data analytics can support informed decision-making, sales optimization, customer understanding, and business strategy.

## 12. Project Deliverables

- Descriptive Statistics
- Numerical Distribution Analysis
- Categorical Analysis
- SQL Business Analysis
- Correlation Matrix
- Heatmap
- Scatter Plots
- Static Business Intelligence Dashboard
- EDA Report
