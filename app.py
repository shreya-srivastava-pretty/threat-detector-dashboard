import streamlit as st
import pandas as pd

# Load data
features = pd.read_csv("features.csv")

# Title
st.title("Insider Threat Detection Dashboard")

# Metrics
st.metric("Total Employees", len(features))

st.metric(
    "High Risk Users",
    len(features[features["risk_level"] == "HIGH"])
)

st.metric(
    "Average Risk Score",
    round(features["risk_score"].mean(), 2)
)

# Top Risk Users
st.subheader("Top Risk Users")

top_users = features.sort_values(
    by="risk_score",
    ascending=False
).head(10)

st.dataframe(top_users)

# Risk Distribution
st.subheader("Risk Level Distribution")

st.bar_chart(
    features["risk_level"].value_counts()
)

# Risk Score Chart
st.subheader("Top 10 Risk Scores")

st.bar_chart(
    top_users.set_index("user")["risk_score"]
)

# Employee Search
st.subheader("Employee Lookup")

selected_user = st.selectbox(
    "Select Employee",
    features["user"].unique()
)

st.write(
    features[features["user"] == selected_user]
)

# Download Report
st.download_button(
    "Download Risk Report",
    features.to_csv(index=False),
    "risk_report.csv",
    "text/csv"
)