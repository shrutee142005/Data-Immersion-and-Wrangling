import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

# Numerical columns
columns = ["Age", "Quantity", "Total_Sales"]

for column in columns:

    plt.figure(figsize=(8, 5))

    plt.hist(df[column], bins=20, edgecolor="black")

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(output_dir / f"{column}_distribution.png")
    plt.close()

print("Distribution graphs created successfully!")

print("Saved in:", output_dir)