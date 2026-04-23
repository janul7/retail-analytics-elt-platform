import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://retail:retail123@localhost:5432/retail_analytics"
)

daily_sales = pd.read_sql(
    "select * from analytics_dev.mart_daily_sales order by order_date",
    engine,
)

customer_ltv = pd.read_sql(
    """
    select *
    from analytics_dev.mart_customer_ltv
    order by lifetime_value desc
    limit 20
    """,
    engine,
)

st.set_page_config(page_title="Retail Analytics ELT Platform", layout="wide")
st.title("Retail Analytics ELT Platform")

col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"{daily_sales['total_revenue'].sum():,.2f}")
col2.metric("Total Orders", int(daily_sales['total_orders'].sum()))

st.subheader("Daily Revenue")
st.line_chart(daily_sales.set_index("order_date")[["total_revenue"]])

st.subheader("Top 20 Customers by Lifetime Value")
st.bar_chart(customer_ltv.set_index("customer_id")[["lifetime_value"]])

st.subheader("Underlying Data")
st.dataframe(daily_sales.tail(30))