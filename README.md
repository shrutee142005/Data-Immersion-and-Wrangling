# Data Immersion, Data Wrangling & Exploratory Data Analysis

## Project Overview
This project focuses on the complete data analytics workflow using a retail sales dataset. It includes data immersion, data cleaning, data wrangling, data validation, exploratory data analysis (EDA), statistical analysis, SQL-based business analysis, correlation analysis, and dashboard development.

The objective is to transform raw data into reliable information and extract meaningful business insights to support data-driven decision-making.

## Project Objectives
- Understand and inspect raw datasets.
- Identify and handle missing values, duplicates, and data quality issues.
- Clean, transform, and validate datasets.
- Perform exploratory data analysis.
- Analyze sales performance using SQL queries.
- Explore relationships between numerical variables.
- Create visualizations and a static business intelligence dashboard.
- Communicate findings through reports and business insights.

## Dataset Description
The project uses a retail sales dataset containing **1,000 records and 12 original columns**.

### Dataset Attributes
- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

The cleaned dataset also contains additional audit and data quality tracking columns.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- SQL
- Excel
- Visual Studio Code
- Git & GitHub

## Task 1: Data Immersion & Data Wrangling

### Data Cleaning
- Inspected dataset structure, columns, data types, and statistical summaries.
- Identified missing values in Age and City.
- Imputed missing Age values using gender-wise median values.
- Replaced missing City values with "Unknown".
- Checked duplicate records.
- Investigated repeated Order_ID values and flagged them without deleting valid transactions.
- Standardized text values by removing unnecessary whitespace.
- Converted Order_Date into a proper date format.
- Checked invalid age, quantity, and unit price values.
- Verified Total_Sales using Quantity × Unit_Price.
- Added audit flags to track data cleaning changes.

### Data Validation
- Verified missing values.
- Checked exact duplicate records.
- Validated Age, Quantity, and Unit_Price values.
- Checked sales calculation consistency.
- Recorded data quality changes using audit flags.

## Task 2: Exploratory Data Analysis (EDA) & Business Intelligence

### Descriptive Statistics
Performed statistical analysis to understand:
- Mean
- Median
- Standard deviation
- Minimum and maximum values
- Frequency distributions
- Unique values
- Missing values

### Univariate Analysis
Analyzed individual variables:
- Age distribution
- Quantity distribution
- Total Sales distribution
- Category frequency
- Product frequency
- City frequency
- Gender distribution

### Business Analysis Using SQL
Created SQL queries to answer seven business questions:

1. Which category generates the highest revenue?
2. Which city generates the highest sales?
3. Which product generates the highest revenue?
4. How do sales change month by month?
5. How does revenue differ by gender?
6. Which age group contributes the highest revenue?
7. Which category has the highest average transaction value?

SQL concepts used:
`SELECT`, `SUM`, `AVG`, `COUNT`, `GROUP BY`, `ORDER BY`, `CASE`, and `strftime`.

### Multivariate & Correlation Analysis
Explored relationships between numerical variables:
- Age and Total Sales
- Quantity and Total Sales
- Unit Price and Total Sales
- Correlation matrix
- Correlation heatmap
- Scatter plots

### Dashboard
Created a static business intelligence dashboard containing:
- Total Revenue
- Total Records
- Average Sales
- Top Revenue Category
- Revenue by Category
- Monthly Sales Trend
- Revenue by Product
- Revenue by City

## Key Business Insights

- **Electronics** generated the highest category revenue of approximately ₹5.08 crore.
- **Laptop** was the highest revenue-generating product.
- **Patna** recorded the highest total revenue among the cities.
- **March 2025** recorded the highest monthly revenue in the analyzed period.
- The **36–45 age group** contributed the highest total revenue.
- **Male customers** contributed slightly higher total revenue than female customers.
- **Grocery** recorded the highest average transaction value among categories.
- Unit Price and Quantity showed positive relationships with Total Sales.
- Age showed almost no linear correlation with Total Sales.

## Project Structure

```text
Data-Immersion-and-Wrangling/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── sales_analysis.db
│
├── notebooks/
│
├── reports/
│   ├── EDA_Report.md
│   ├── SQL_Business_Analysis.md
│   ├── categorical_statistics.csv
│   ├── numerical_statistics.csv
│   ├── correlation_matrix.csv
│   └── figures/
│       ├── static_dashboard.png
│       ├── correlation_heatmap.png
│       ├── monthly_sales_trend.png
│       └── other analysis charts
│
├── scripts/
│   ├── inspect_data.py
│   ├── data_check.py
│   ├── clean_data.py
│   ├── validate_cleaned.py
│   ├── eda_analysis.py
│   ├── descriptive_statistics.py
│   ├── univariate_analysis.py
│   ├── categorical_analysis.py
│   ├── sql_analysis.py
│   ├── correlation_analysis.py
│   ├── scattering_analysis.py
│   └── static_dashboard.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Project Outputs
- Cleaned retail sales dataset.
- Data quality validation results.
- Descriptive statistical summaries.
- SQL business analysis with seven queries.
- Correlation matrix and heatmap.
- Univariate and categorical analysis charts.
- Scatter plots.
- Static business intelligence dashboard.
- EDA report and business insights.

## Conclusion
This project demonstrates an end-to-end data analytics workflow, from raw data inspection and cleaning to statistical analysis, SQL querying, visualization, and business intelligence.

By combining data wrangling and exploratory data analysis, the project transforms raw retail data into actionable insights that can support business decision-making.

## Author
**Data Immersion & Data Wrangling Project**  
ApexPlanet Software Pvt. Ltd. Internship
