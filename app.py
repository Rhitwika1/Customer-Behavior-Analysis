import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Customer Behavior Analysis", layout="wide")

st.title("Customer Behavior Analysis Dashboard")

# Load dataset
@st.cache_data 
def load_data(): 
    return pd.read_csv("customer_shopping_behavior.csv") 
df = load_data()


if df is None:
    st.stop()
# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("Filter Options")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df = df[df["Gender"].isin(gender_filter)]

# Gender Distribution
st.subheader("Gender Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x="Gender", data=df, ax=ax1)
st.pyplot(fig1)

# Age Distribution
st.subheader("Age Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df["Age"], bins=20, ax=ax2)
st.pyplot(fig2)

# Purchase Amount Distribution
st.subheader("Purchase Amount Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(df["Purchase Amount (USD)"], bins=20, ax=ax3)
st.pyplot(fig3)

# Product Category Analysis
st.subheader("Top Product Categories")
fig4, ax4 = plt.subplots()
sns.countplot(
    y="Category",
    data=df,
    order=df["Category"].value_counts().index,
    ax=ax4
)
st.pyplot(fig4)

# Key Metrics
st.subheader("Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", df["Customer ID"].nunique())
col2.metric("Total Revenue", f"{df['Purchase Amount (USD)'].sum():,.2f}")
col3.metric("Average Purchase", f"{df['Purchase Amount (USD)'].mean():,.2f}")

st.success("Project developed by Rhitwika")