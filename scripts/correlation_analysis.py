import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "cleaned" / "cleaned_sales_dataset.csv"
output_dir = BASE_DIR / "reports" / "figures"

output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(input_file)

# Select numerical columns
numerical_columns = ["Age", "Quantity", "Unit_Price", "Total_Sales"]

numerical_df = df[numerical_columns]

# Calculate correlation
correlation_matrix = numerical_df.corr()

print("\n========== CORRELATION ANALYSIS ==========")
print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))

# Save correlation matrix
correlation_matrix.to_csv(
    BASE_DIR / "reports" / "correlation_matrix.csv"
)

# Create heatmap using matplotlib
plt.figure(figsize=(8, 6))

plt.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)

plt.colorbar(label="Correlation")

plt.xticks(
    range(len(numerical_columns)),
    numerical_columns,
    rotation=45
)

plt.yticks(
    range(len(numerical_columns)),
    numerical_columns
)

# Add correlation values
for i in range(len(numerical_columns)):
    for j in range(len(numerical_columns)):
        plt.text(
            j, i,
            round(correlation_matrix.iloc[i, j], 2),
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig(output_dir / "correlation_heatmap.png")
plt.close()

print("\nCorrelation analysis completed!")
print("Heatmap saved inside:", output_dir)