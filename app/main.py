import streamlit as st
from utils import combine_countries, plot_boxplot
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("🌞 Solar Farm Insights Dashboard")

# --- Sidebar: Country & Metric Selection ---
st.sidebar.header("Filter Options")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

selected_metric = st.sidebar.selectbox(
    "Select Metric",
    options=["GHI", "DNI", "DHI"],
    index=0
)

# --- Load & combine data ---
if not selected_countries:
    st.warning("Please select at least one country!")
    st.stop()

df = combine_countries(selected_countries)

# --- Debug: preview data ---
st.subheader("Data Preview")
st.dataframe(df.head())
st.write("Data shape:", df.shape)

# --- Show Top 5 Observations Table ---
st.subheader(f"Top 5 observations for {selected_metric}")
top_df = df[['Timestamp', 'Country', selected_metric]].sort_values(
    by=selected_metric, ascending=False
).head(5)
st.dataframe(top_df)

# --- Show Boxplot ---
st.subheader(f"{selected_metric} Distribution by Country")
fig = plot_boxplot(df, selected_metric)
st.pyplot(fig)
