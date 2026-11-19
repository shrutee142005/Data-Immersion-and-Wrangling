# Data Immersion & Data Wrangling

## Project Overview
This project focuses on data immersion, data cleaning, data wrangling, and exploratory data analysis (EDA) using a retail sales dataset. The objective is to transform raw data into a clean, reliable dataset and analyze sales patterns across products, categories, cities, genders, age groups, and months.

## Objectives
- Understand and inspect the raw dataset.
- Identify missing values, duplicates, and data quality issues.
- Clean and preprocess the dataset.
- Validate the cleaned data.
- Perform exploratory data analysis.
- Generate visualizations and meaningful business insights.

## Dataset Description
The dataset contains 1,000 records and 12 original columns.

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

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Excel
- Visual Studio Code

## Data Cleaning & Wrangling
The following preprocessing steps were performed:

1. Inspected the dataset structure, columns, data types, and statistical information.
2. Identified missing values in Age and City.
3. Imputed missing Age values using gender-wise median values.
4. Replaced missing City values with "Unknown".
5. Checked duplicate records.
6. Investigated repeated Order_ID values and flagged them without deleting valid transactions.
7. Standardized text values by removing unnecessary whitespace.
8. Converted Order_Date into a proper date format.
9. Checked for invalid age, quantity, and unit price values.
10. Verified Total_Sales using Quantity × Unit_Price.
11. Added audit flags to track data cleaning changes.

## Data Validation
The cleaned dataset was validated to ensure:

- No missing values remained.
- No exact duplicate rows were present.
- Age values were within the valid range.
- Quantity and Unit_Price values were valid.
- Sales calculations were consistent.
- Data cleaning changes were recorded using audit flags.

## Exploratory Data Analysis (EDA)
The analysis was performed across different dimensions:

- Sales by Product
- Sales by Category
- Sales by City
- Monthly Sales Trend
- Sales by Gender
- Sales by Age Group

## Key Insights
- Laptop generated the highest sales among products.
- Electronics was the highest revenue-generating category.
- Patna recorded the highest total sales among cities.
- Monthly sales fluctuated, with higher sales during certain months.
- Sales performance differed across gender and age groups.

## Project Structure

```text
Data-Immersion-warngling/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
│
├── reports/
│   └── figures/
│
├── scripts/
│   ├── inspect_data.py
│   ├── data_check.py
│   ├── clean_data.py
│   ├── validate_cleaned.py
│   └── eda_analysis.py
│
├── README.md
└── requirements.txt
```

## Project Outputs
- Cleaned dataset in CSV format.
- Data quality validation results.
- Exploratory data analysis results.
- Sales visualization charts.
- Summary report containing key insights.

## Conclusion
This project demonstrates the complete data analysis workflow, beginning with raw data inspection and ending with data cleaning, validation, exploratory analysis, and visualization. The process improves data quality and helps identify meaningful sales patterns that can support better business decision-making.

## Author
Data Immersion & Data Wrangling Project  
ApexPlanet Software Pvt. Ltd. Internship
