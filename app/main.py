import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
import streamlit as st
import plotly.express as px
from ml.predict import predict_risk

# PAGE CONFIG & SIDEBAR

st.set_page_config(page_title="Transformer Early Warning", layout="wide")
st.title("AI-Based Transformer Failure Early Warning System")

st.sidebar.header("Controls")

risk_mode = st.sidebar.radio(
    "Risk Calculation Mode",
    ["Rule-Based", "AI-Based"]
)

# FUNCTION DEFINITIONS

def calculate_risk(row):
    risk = 0
    if row["load_percent"] > 80:
        risk += 30
    elif row["load_percent"] > 60:
        risk += 15

    if row["oil_temp_c"] > 70:
        risk += 30
    elif row["oil_temp_c"] > 55:
        risk += 15

    if row["rainfall_mm"] > 20:
        risk += 20
    elif row["rainfall_mm"] > 5:
        risk += 10

    if row["age_years"] > 15:
        risk += 20
    elif row["age_years"] > 8:
        risk += 10

    return risk


def risk_level(score):
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"


def ai_risk_row(row):
    result = predict_risk({
        "load_percent": row["load_percent"],
        "oil_temp_c": row["oil_temp_c"],
        "rainfall_mm": row["rainfall_mm"],
        "age_years": row["age_years"]
    })
    return pd.Series([result["risk_label"], result["risk_probability"]])

# AI RISK EXPLANATION

def explain_ai_risk(row):
    reasons = []

    if row["load_percent"] > 70:
        reasons.append("High electrical load")

    if row["oil_temp_c"] > 60:
        reasons.append("Elevated oil temperature")

    if row["rainfall_mm"] > 15:
        reasons.append("Heavy rainfall / moisture risk")

    if row["age_years"] > 10:
        reasons.append("Aging transformer")

    if not reasons:
        return "Operating within safe limits"

    return ", ".join(reasons)


# LOAD DATA

data = pd.read_csv("data/sample_transformer_data.csv")

# RULE-BASED RISK
# Explainability column
data["ai_explanation"] = data.apply(explain_ai_risk, axis=1)
data["risk_score"] = data.apply(calculate_risk, axis=1)
data["risk_level"] = data["risk_score"].apply(risk_level)

# AI-BASED RISK

data[["ai_risk", "ai_confidence"]] = data.apply(ai_risk_row, axis=1)

data["ai_risk_label"] = data["ai_risk"].map({
    1: "HIGH",
    0: "LOW"
})

# FINAL RISK (TOGGLE OUTPUT)

if risk_mode == "AI-Based":
    data["final_risk"] = data["ai_risk_label"]
else:
    data["final_risk"] = data["risk_level"]

# KPIs (USING FINAL RISK)

total = len(data)
high = (data["final_risk"] == "HIGH").sum()
medium = (data["final_risk"] == "MEDIUM").sum()
low = (data["final_risk"] == "LOW").sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Transformers", total)
col2.metric("High Risk", high)
col3.metric("Medium Risk", medium)
col4.metric("Low Risk", low)

# CHARTS

st.divider()
st.subheader("Risk Distribution")

risk_counts = data["final_risk"].value_counts().reset_index()
risk_counts.columns = ["final_risk", "count"]

fig = px.bar(
    risk_counts,
    x="final_risk",
    y="count",
    color="final_risk",
    title="Transformer Risk Distribution"
)
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Load vs Oil Temperature")

scatter_fig = px.scatter(
    data,
    x="load_percent",
    y="oil_temp_c",
    color="final_risk",
    size="ai_confidence",
    hover_data=["transformer_id", "age_years", "rainfall_mm"],
    title="Transformer Load vs Oil Temperature",
)
st.plotly_chart(scatter_fig, use_container_width=True)

# FILTERS

st.sidebar.header("Filters")

selected_risk = st.sidebar.selectbox(
    "Select Risk Level",
    options=["ALL", "HIGH", "MEDIUM", "LOW"]
)

filtered_data = data.copy()

if selected_risk != "ALL":
    filtered_data = filtered_data[
        filtered_data["final_risk"] == selected_risk
    ]

# TABLE

st.subheader("Transformer Risk Overview")

def color_risk(val):
    if val == "HIGH":
        return "background-color: #ff4d4d; color: white;"
    elif val == "MEDIUM":
        return "background-color: #ffd966;"
    else:
        return "background-color: #7ddc7d;"

styled_df = filtered_data.style.applymap(
    color_risk,
    subset=["final_risk"]
)

#st.dataframe(styled_df, use_container_width=True)
st.dataframe(
    filtered_data[[
        "transformer_id",
        "final_risk",
        "ai_confidence",
        "ai_explanation"
    ]],
    use_container_width=True
)
st.info(
    "AI explanations are generated using operational parameters such as load, oil temperature, rainfall, and transformer age."
)

