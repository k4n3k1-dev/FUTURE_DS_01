import streamlit as st
import pandas as pd

st.set_page_config(page_title="Superstore Dashboard", layout="wide")

st.title("📊 Superstore Sales Dashboard")

# Load processed data
monthly_sales = pd.read_csv('monthly_sales.csv')
top_products = pd.read_csv('top_products.csv')
category = pd.read_csv('category_performance.csv')
region = pd.read_csv('region_performance.csv')

# ---- Revenue Trend ----
st.subheader("📈 Monthly Revenue Trend")
st.line_chart(monthly_sales.set_index('Order Date'))

# ---- Top Products ----
st.subheader("🏆 Top 10 Products")
st.bar_chart(top_products.set_index('Product Name'))

# ---- Category ----
st.subheader("🧩 Category Performance")
st.bar_chart(category.set_index('Category'))

# ---- Region ----
st.subheader("🌍 Region Performance")
st.bar_chart(region.set_index('Region'))
