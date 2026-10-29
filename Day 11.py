# DAY 11: DATA VISUALIZATION WITH MATPLOTLIB AND SEABORN

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Practical 1: Create Dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 13000, 18000, 22000, 20000],
    "Profit": [2000, 3000, 2500, 4000, 5000, 4500],
    "Customers": [100, 120, 110, 150, 180, 170],
    "Advertising": [1000, 1500, 1200, 2000, 2500, 2200]
}

df = pd.DataFrame(data)

print("\n--- PRACTICAL 1: DATASET ---")
print(df)

# Practical 2: Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Sales"], label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.tight_layout()
plt.show()

# Practical 3: Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker="o", label="Sales")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Practical 4: Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=5, edgecolor="black")
plt.title("Distribution of Monthly Sales")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Practical 5: Box Plot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Sales"])
plt.title("Box Plot of Monthly Sales")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.show()

# Practical 6: Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Advertising", y="Sales")
plt.title("Advertising Expenses vs Sales")
plt.xlabel("Advertising Expenses")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.show()

# Practical 7: Correlation Heatmap
numeric_data = df[
    ["Sales", "Profit", "Customers", "Advertising"]
]

correlation_matrix = numeric_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Practical 8: Sales and Profit Line Chart
plt.figure(figsize=(8, 5))

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    df["Month"],
    df["Profit"],
    marker="s",
    label="Profit"
)

plt.title("Monthly Sales and Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nDay 11 Data Visualization Task Completed.")