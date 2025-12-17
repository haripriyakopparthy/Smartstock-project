import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="SmartStock Inventory Dashboard", layout="wide")

st.title("📦 SmartStock – Inventory Optimization Dashboard")

# Upload CSV
file = st.file_uploader("Upload Inventory CSV File", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])

    st.subheader("📄 Inventory Data")
    st.dataframe(df)

    # Inventory Status
    def stock_status(stock):
        if stock < 20:
            return "Low Stock"
        elif stock > 100:
            return "Overstock"
        else:
            return "Normal"

    df['Stock Status'] = df['Stock'].apply(stock_status)

    # Filters
    product_filter = st.selectbox("Filter by Product", ["All"] + list(df['Product'].unique()))
    if product_filter != "All":
        df = df[df['Product'] == product_filter]

    # Alerts
    st.subheader("🚨 Restocking Alerts")
    low_stock = df[df['Stock Status'] == "Low Stock"]
    if not low_stock.empty:
        st.error("⚠ Low Stock Detected! Immediate Restocking Required")
        st.dataframe(low_stock)
    else:
        st.success("✅ All products have sufficient stock")

    # Stock Trend Chart
    st.subheader("📈 Stock Level Trend")
    fig1 = px.line(df, x='Date', y='Stock', color='Product', title="Stock Over Time")
    st.plotly_chart(fig1, use_container_width=True)

    # Sales vs Stock
    st.subheader("📊 Sales vs Stock Analysis")
    fig2 = px.scatter(df, x='Sales', y='Stock', color='Stock Status',
                      title="Sales vs Stock Distribution")
    st.plotly_chart(fig2, use_container_width=True)

    # Stock Status Distribution
    st.subheader("🥧 Inventory Status Distribution")
    fig3 = px.pie(df, names='Stock Status', title="Stock Status Breakdown")
    st.plotly_chart(fig3)

    # Demand Analysis
    st.subheader("📉 Demand Pattern Analysis")
    demand = df.groupby('Product')['Sales'].mean().reset_index()
    fig4 = px.bar(demand, x='Product', y='Sales', title="Average Sales per Product")
    st.plotly_chart(fig4)

    # Recommendation
    st.subheader("📌 Restocking Recommendations")
    df['Recommendation'] = df['Stock Status'].apply(
        lambda x: "Restock Immediately" if x == "Low Stock" else
        "Reduce Order Quantity" if x == "Overstock" else
        "Stock Level Optimal"
    )

    st.dataframe(df[['Product', 'Stock', 'Sales', 'Stock Status', 'Recommendation']])