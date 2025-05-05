import pandas as pd
import streamlit as st
import plotly.express as px

st.title("🚚 EZ Street Deliveries Dashboard")

st.write("Upload your delivery data CSV file below:")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Delivery Data Preview")
    st.write(df.head())

    total_orders = len(df)
    avg_time = df["Time_taken_min"].mean()
    cancelled = len(df[df["Status"] == "Cancelled"])

    st.subheader("📊 Key Metrics")
    st.metric("Total Orders", total_orders)
    st.metric("Avg. Delivery Time (min)", round(avg_time, 2))
    st.metric("Cancelled Orders", cancelled)

    st.subheader("Deliveries by Driver")
    chart = df["Driver"].value_counts().reset_index()
    chart.columns = ["Driver", "Deliveries"]
    fig = px.bar(chart, x="Driver", y="Deliveries", color="Driver", text="Deliveries")
    st.plotly_chart(fig)

    st.subheader("Status Breakdown")
    fig2 = px.pie(df, names="Status", title="Delivery Status")
    st.plotly_chart(fig2)
else:
    st.info("Please upload a CSV file to view the dashboard.")
