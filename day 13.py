
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------
# 1. LOAD DATASET
# ---------------------------------------

file_path = os.path.join(
    os.path.expanduser("~"),
    "Downloads",
    "Day12_Sales_Dataset.xlsx"
)

df = pd.read_excel(file_path)

print("\n========== DATASET OVERVIEW ==========")
print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)


# ---------------------------------------
# 2. DATA QUALITY CHECKS
# ---------------------------------------

print("\n========== DATA QUALITY ==========")

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

# Remove exact duplicate rows, if any
df = df.drop_duplicates().copy()

# Convert date columns to datetime
for col in ["Order_Date", "Ship_Date"]:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")

# Convert numeric columns to numeric format
numeric_columns = [
    "Quantity", "Discount", "Sales", "Profit"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Fill missing numeric values with column median
for col in numeric_columns:
    if col in df.columns and df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

print("\nDataset shape after cleaning:", df.shape)
print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ---------------------------------------
# 3. DESCRIPTIVE STATISTICS
# ---------------------------------------

print("\n========== DESCRIPTIVE STATISTICS ==========")
print(df.describe(include="all"))


# ---------------------------------------
# 4. FIVE BUSINESS QUESTIONS USING PANDAS
# ---------------------------------------

print("\n========== BUSINESS QUESTION 1 ==========")
print("Which region generates the highest sales?")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(
    ascending=False
)
print(region_sales)


print("\n========== BUSINESS QUESTION 2 ==========")
print("Which product category generates the highest sales?")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(
    ascending=False
)
print(category_sales)


print("\n========== BUSINESS QUESTION 3 ==========")
print("How do sales change over time?")

monthly_sales = (
    df.dropna(subset=["Order_Date"])
      .set_index("Order_Date")["Sales"]
      .resample("MS")
      .sum()
)
print(monthly_sales)


print("\n========== BUSINESS QUESTION 4 ==========")
print("Which customer segment generates the highest profit?")

segment_profit = df.groupby("Segment")["Profit"].sum().sort_values(
    ascending=False
)
print(segment_profit)


print("\n========== BUSINESS QUESTION 5 ==========")
print("Which payment method is used for the highest sales amount?")

payment_sales = df.groupby("Payment_Method")["Sales"].sum().sort_values(
    ascending=False
)
print(payment_sales)


# ---------------------------------------
# 5. SQL ANALYSIS USING SQLITE
# ---------------------------------------

print("\n========== SQL ANALYSIS ==========")

connection = sqlite3.connect(":memory:")
df.to_sql("sales", connection, index=False, if_exists="replace")

queries = {
    "Sales by Region": """
        SELECT Region, ROUND(SUM(Sales), 2) AS Total_Sales
        FROM sales
        GROUP BY Region
        ORDER BY Total_Sales DESC
    """,

    "Sales by Category": """
        SELECT Category, ROUND(SUM(Sales), 2) AS Total_Sales
        FROM sales
        GROUP BY Category
        ORDER BY Total_Sales DESC
    """,

    "Profit by Segment": """
        SELECT Segment, ROUND(SUM(Profit), 2) AS Total_Profit
        FROM sales
        GROUP BY Segment
        ORDER BY Total_Profit DESC
    """
}

for title, query in queries.items():
    print("\n" + title)
    print(pd.read_sql_query(query, connection))

connection.close()


# ---------------------------------------
# 6. CREATE VISUALIZATIONS
# ---------------------------------------

output_folder = os.path.join(
    os.path.expanduser("~"),
    "Downloads",
    "Day13_EDA_Charts"
)
os.makedirs(output_folder, exist_ok=True)

# Chart 1: Sales by Region
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "sales_by_region.png"))
plt.show()
plt.close()

# Chart 2: Sales by Category
category_sales.plot(kind="bar", title="Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "sales_by_category.png"))
plt.show()
plt.close()

# Chart 3: Monthly Sales Trend
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "monthly_sales_trend.png"))
plt.show()
plt.close()


# ---------------------------------------
# 7. SUMMARY AND LIMITATIONS
# ---------------------------------------

print("\n========== SUMMARY ==========")
print("Total records analyzed:", len(df))
print("Total sales:", round(df["Sales"].sum(), 2))
print("Total profit:", round(df["Profit"].sum(), 2))
print("Distinct orders:", df["Order_ID"].nunique())

print("\nRegion with highest sales:", region_sales.idxmax())
print("Category with highest sales:", category_sales.idxmax())
print("Segment with highest profit:", segment_profit.idxmax())
print("Payment method with highest sales:", payment_sales.idxmax())

print("\n========== LIMITATIONS ==========")
print("1. The dataset is simulated practice data, not real company data.")
print("2. Findings describe only the available dataset.")
print("3. The analysis shows associations and summaries, not causal relationships.")

print("\nCharts saved in:", output_folder)
print("\nDay 13 EDA analysis completed successfully!")


