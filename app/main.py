import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import pandas as pd
import streamlit as st
import plotly.express as px
from ml.predict import predict_risk

st.set_page_config(page_title="Transformer Early Warning", layout="wide")
st.title("AI-Based Transformer Failure Early Warning System")


# Load data

data = pd.read_csv("data/sample_transformer_data.csv")


# AI Prediction

def ai_risk_row(row):
    result = predict_risk({
        "load_percent": row["load_percent"],
        "oil_temp_c": row["oil_temp_c"],
        "rainfall_mm": row["rainfall_mm"],
        "age_years": row["age_years"]
    })
    return pd.Series([result["risk_label"], result["risk_probability"]])

data[["ai_risk", "ai_confidence"]] = data.apply(ai_risk_row, axis=1)

data["ai_risk_label"] = data["ai_risk"].map({
    1: "HIGH",
    0: "LOW"
})


# KPIs (AI-based)

total = len(data)
high = (data["ai_risk_label"] == "HIGH").sum()
low = (data["ai_risk_label"] == "LOW").sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Transformers", total)
col2.metric("High Risk (AI)", high)
col3.metric("Low Risk (AI)", low)


# Charts

st.divider()
st.subheader("AI Risk Distribution")

risk_counts = data["ai_risk_label"].value_counts().reset_index()
risk_counts.columns = ["ai_risk_label", "count"]

fig = px.bar(
    risk_counts,
    x="ai_risk_label",
    y="count",
    color="ai_risk_label",
    title="AI-Based Transformer Risk Distribution"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Load vs Oil Temperature (AI Colored)")

scatter_fig = px.scatter(
    data,
    x="load_percent",
    y="oil_temp_c",
    color="ai_risk_label",
    size="ai_confidence",
    hover_data=["transformer_id", "age_years", "rainfall_mm"],
    title="Transformer Load vs Oil Temperature (AI Prediction)",
)
st.plotly_chart(scatter_fig, use_container_width=True)


# Filters

st.sidebar.header("Filters")

selected_risk = st.sidebar.selectbox(
    "Select AI Risk Level",
    options=["ALL", "HIGH", "LOW"]
)

filtered_data = data.copy()

if selected_risk != "ALL":
    filtered_data = filtered_data[
        filtered_data["ai_risk_label"] == selected_risk
    ]


# Table

st.subheader("Transformer Risk Overview (AI-Based)")

def color_risk(val):
    if val == "HIGH":
        return "background-color: #ff4d4d; color: white;"
    else:
        return "background-color: #7ddc7d;"

styled_df = filtered_data.style.applymap(
    color_risk,
    subset=["ai_risk_label"]
)

st.dataframe(styled_df, use_container_width=True)
