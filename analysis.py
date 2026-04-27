import pandas as pd

# Load dataset
df = pd.read_csv('superstore.csv', encoding='latin1')

# Data cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.dropna()

# -------------------------
# 1. Monthly Sales Trend
# -------------------------
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.to_csv('monthly_sales.csv')

# -------------------------
# 2. Top Products
# -------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.to_csv('top_products.csv')

# -------------------------
# 3. Category Performance
# -------------------------
category_perf = df.groupby('Category')[['Sales', 'Profit']].sum()
category_perf.to_csv('category_performance.csv')

# -------------------------
# 4. Region Performance
# -------------------------
region_perf = df.groupby('Region')[['Sales', 'Profit']].sum()
region_perf.to_csv('region_performance.csv')

print("Analysis complete. Files saved in current folder.")
