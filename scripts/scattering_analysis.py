import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

# Variables to compare with sales
columns = ["Age", "Quantity", "Unit_Price"]

for column in columns:

    plt.figure(figsize=(8, 5))

    plt.scatter(df[column], df["Total_Sales"], alpha=0.6)

    plt.title(f"{column} vs Total Sales")
    plt.xlabel(column)
    plt.ylabel("Total Sales")

    plt.grid(True)
    plt.tight_layout()

    plt.savefig(output_dir / f"{column}_vs_sales_scatter.png")
    plt.close()

print("Scatter plots created successfully!")
print("Saved in:", output_dir)