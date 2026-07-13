import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(
    page_title="Nassau Candy Distributor Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Nassau Candy Distributor Dashboard")

df = pd.read_csv("Nassau Candy Distributor.csv")

st.sidebar.header("Filters")

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

st.subheader("Dataset Preview")
st.dataframe(df)
st.subheader("Column Names")
st.write(df.columns)
st.subheader("Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${df['Gross Profit'].sum():,.2f}")
col3.metric("Total Units", int(df['Units'].sum()))
st.subheader("Sales by Region")

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Total Sales by Region"
)

st.plotly_chart(fig, key="sales_chart")
st.subheader("Profit by Region")

region_profit = df.groupby("Region")["Gross Profit"].sum().reset_index()

fig2 = px.bar(
    region_profit,
    x="Region",
    y="Gross Profit",
    title="Total Profit by Region",
    color="Region"
)
st.plotly_chart(fig2, key="profit_chart")
st.subheader("Sales Distribution by Region")

fig3 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales Distribution by Region"
)

st.plotly_chart(fig3)
st.subheader("Top 10 Products by Sales")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    color="Sales"
)

st.plotly_chart(fig4)
st.subheader("Sales by Ship Mode")

ship_sales = df.groupby("Ship Mode")["Sales"].sum().reset_index()

fig5 = px.bar(
    ship_sales,
    x="Ship Mode",
    y="Sales",
    title="Sales by Ship Mode",
    color="Ship Mode"
)

st.plotly_chart(fig5)
st.subheader("Top 10 Cities by Sales")

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig6 = px.bar(
    city_sales,
    x="City",
    y="Sales",
    title="Top 10 Cities by Sales",
    color="Sales"
)

st.plotly_chart(fig6)
st.subheader("Monthly Sales Trend")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig7 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(fig7)
st.subheader("Top 10 States by Sales")

state_sales = (
    df.groupby("State/Province")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig8 = px.bar(
    state_sales,
    x="State/Province",
    y="Sales",
    title="Top 10 States by Sales",
    color="Sales"
)

st.plotly_chart(fig8)
st.subheader("Top 10 Customers by Sales")

top_customers = (
    df.groupby("Customer ID")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig9 = px.bar(
    top_customers,
    x="Customer ID",
    y="Sales",
    title="Top 10 Customers by Sales",
    color="Sales"
)

st.plotly_chart(fig9)
st.markdown("---")
st.header("📌 Key Insights")

st.write("✅ The highest sales are generated from the top-performing regions.")
st.write("✅ Some products contribute significantly more revenue than others.")
st.write("✅ Sales vary across different ship modes.")
st.write("✅ A few cities and states contribute a major share of total sales.")
st.write("✅ Monthly sales trend helps identify seasonal business performance.")
st.markdown("---")

st.markdown("---")
st.success("✅ Data Analytics Dashboard Developed by Saniya More")
