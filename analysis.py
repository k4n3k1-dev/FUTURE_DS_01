import pandas as pd

# Load dataset safely
df = pd.read_csv('superstore.csv', encoding='latin1')

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Drop missing values
df = df.dropna()

# -------------------------
# 1. Monthly Sales Trend
# -------------------------
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
monthly_sales.to_csv('monthly_sales.csv', index=False)

# -------------------------
# 2. Top Products
# -------------------------
top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_products.to_csv('top_products.csv', index=False)

# -------------------------
# 3. Category Performance
# -------------------------
category_perf = (
    df.groupby('Category')[['Sales', 'Profit']]
    .sum()
    .reset_index()
)
category_perf.to_csv('category_performance.csv', index=False)

# -------------------------
# 4. Region Performance
# -------------------------
region_perf = (
    df.groupby('Region')[['Sales', 'Profit']]
    .sum()
    .reset_index()
)
region_perf.to_csv('region_performance.csv', index=False)

print("✅ Analysis complete. Files saved.")
