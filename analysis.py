import pandas as pd

# Load dataset
df = pd.read_csv('../data/superstore.csv', encoding='latin1')

# Data cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'])
df = df.dropna()

# -------------------------
# 1. Monthly Sales Trend
# -------------------------
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.to_csv('../outputs/monthly_sales.csv')

# -------------------------
# 2. Top Products
# -------------------------
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.to_csv('../outputs/top_products.csv')

# -------------------------
# 3. Category Performance
# -------------------------
category_perf = df.groupby('Category')[['Sales', 'Profit']].sum()
category_perf.to_csv('../outputs/category_performance.csv')

# -------------------------
# 4. Region Performance
# -------------------------
region_perf = df.groupby('Region')[['Sales', 'Profit']].sum()
region_perf.to_csv('../outputs/region_performance.csv')

print("Analysis complete. Files saved in outputs/")
