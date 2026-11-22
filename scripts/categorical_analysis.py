import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

# Categorical columns
columns = ["Category", "Product", "City", "Gender"]

for column in columns:

    counts = df[column].value_counts()

    plt.figure(figsize=(9, 5))

    counts.plot(kind="bar", edgecolor="black")

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Number of Records")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(output_dir / f"{column}_distribution.png")
    plt.close()

    print(f"\n--- {column} ---")
    print(counts)

print("\nCategorical analysis completed!")
print("Graphs saved in:", output_dir)