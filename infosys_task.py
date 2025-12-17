import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("📦 SmartStock Inventory Optimization Dashboard")

# File upload
file = st.file_uploader("Upload Inventory CSV File", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])

    st.subheader("📄 Inventory Data")
    st.dataframe(df)

    # Product selection
    product = st.selectbox("Select Product", df['Product'].unique())
    product_df = df[df['Product'] == product]

    # ---------- Matplotlib Line Chart ----------
    st.subheader("📉 Stock Level Over Time (Matplotlib)")
    fig, ax = plt.subplots()
    ax.plot(product_df['Date'], product_df['Stock'], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock")
    ax.set_title(f"Stock Trend for {product}")
    st.pyplot(fig)

    # ---------- Scatter Plot ----------
    st.subheader("⚠ Stock Anomalies (Scatter Plot)")
    fig2, ax2 = plt.subplots()
    ax2.scatter(product_df['Sales'], product_df['Stock'])
    ax2.set_xlabel("Sales")
    ax2.set_ylabel("Stock")
    ax2.set_title("Sales vs Stock")
    st.pyplot(fig2)

    # ---------- Plotly Interactive Line Chart ----------
    st.subheader("📊 Interactive Sales vs Stock (Plotly)")
    fig3 = px.line(
        product_df,
        x="Date",
        y=["Sales", "Stock"],
        title="Sales vs Stock Trend",
        markers=True
    )
    st.plotly_chart(fig3)

    # ---------- Stock Status ----------
    def stock_status(stock):
        if stock < 30:
            return "Low"
        elif stock > 150:
            return "Overstock"
        else:
            return "Normal"

    df['Status'] = df['Stock'].apply(stock_status)

    # ---------- Plotly Pie Chart ----------
    st.subheader("🥧 Stock Status Distribution")
    status_count = df['Status'].value_counts().reset_index()
    status_count.columns = ['Status', 'Count']

    fig4 = px.pie(
        status_count,
        names='Status',
        values='Count',
        title='Inventory Status Distribution'
    )
    st.plotly_chart(fig4)

    # ---------- Alerts ----------
    st.subheader("🚨 Stock Alerts")
    latest_stock = product_df.iloc[-1]['Stock']

    if latest_stock < 30:
        st.error("Low Stock! Reorder Immediately ⚠")
    elif latest_stock > 150:
        st.warning("Overstock Detected! Reduce Purchase ⚠")
    else:
        st.success("Stock Level is Normal ✅")