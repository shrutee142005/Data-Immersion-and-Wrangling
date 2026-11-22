import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# KPIs
total_revenue = df["Total_Sales"].sum()
total_records = len(df)
average_sales = df["Total_Sales"].mean()
top_category = df.groupby("Category")["Total_Sales"].sum().idxmax()

# Analysis
category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values()
product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

# Create dashboard
fig = plt.figure(figsize=(16, 10))
fig.suptitle(
    "RETAIL SALES ANALYTICS DASHBOARD",
    fontsize=20,
    fontweight="bold"
)

# KPI Cards
kpis = [
    ("TOTAL REVENUE", f"₹{total_revenue/10000000:.2f} Cr"),
    ("TOTAL RECORDS", f"{total_records:,}"),
    ("AVERAGE SALES", f"₹{average_sales:,.0f}"),
    ("TOP CATEGORY", top_category)
]

positions = [0.08, 0.30, 0.52, 0.74]

for position, (title, value) in zip(positions, kpis):
    fig.text(
        position, 0.88, title,
        fontsize=11, fontweight="bold",
        ha="center"
    )
    fig.text(
        position, 0.82, value,
        fontsize=17, fontweight="bold",
        ha="center"
    )

# Category revenue
ax1 = fig.add_axes([0.07, 0.52, 0.40, 0.24])
category_sales.plot(kind="bar", ax=ax1)
ax1.set_title("Revenue by Category")
ax1.set_ylabel("Revenue")
ax1.tick_params(axis="x", rotation=35)

# Monthly trend
ax2 = fig.add_axes([0.55, 0.52, 0.38, 0.24])
monthly_sales.plot(kind="line", marker="o", ax=ax2)
ax2.set_title("Monthly Sales Trend")
ax2.set_ylabel("Revenue")
ax2.tick_params(axis="x", rotation=45)
ax2.grid(True)

# Product revenue
ax3 = fig.add_axes([0.07, 0.13, 0.40, 0.24])
product_sales.plot(kind="bar", ax=ax3)
ax3.set_title("Revenue by Product")
ax3.set_ylabel("Revenue")
ax3.tick_params(axis="x", rotation=35)

# City revenue
ax4 = fig.add_axes([0.55, 0.13, 0.38, 0.24])
city_sales.plot(kind="bar", ax=ax4)
ax4.set_title("Revenue by City")
ax4.set_ylabel("Revenue")
ax4.tick_params(axis="x", rotation=35)

# Save dashboard
dashboard_file = output_dir / "static_dashboard.png"

plt.savefig(dashboard_file, dpi=300, bbox_inches="tight")
plt.close()

print("Dashboard created successfully!")
print("Total Revenue:", total_revenue)
print("Top Category:", top_category)
print("Saved at:", dashboard_file)