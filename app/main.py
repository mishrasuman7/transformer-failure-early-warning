import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Transformer Early Warning", layout="wide")
st.title("AI-Based Transformer Failure Early Warning System")

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


data = pd.read_csv("data/sample_transformer_data.csv")
data["risk_score"] = data.apply(calculate_risk, axis=1)
data["risk_level"] = data["risk_score"].apply(risk_level)


total = len(data)
high = (data["risk_level"] == "HIGH").sum()
medium = (data["risk_level"] == "MEDIUM").sum()
low = (data["risk_level"] == "LOW").sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Transformers", total)
col2.metric("High Risk", high)
col3.metric("Medium Risk", medium)
col4.metric("Low Risk", low)

st.divider()
st.subheader("Risk Level Distribution")

risk_counts = data["risk_level"].value_counts().reset_index()
risk_counts.columns = ["risk_level", "count"]

fig = px.bar(
    risk_counts,
    x="risk_level",
    y="count",
    color="risk_level",
    title="Number of Transformers by Risk Level",
)

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Load vs Oil Temperature Analysis")

scatter_fig = px.scatter(
    data,
    x="load_percent",
    y="oil_temp_c",
    color="risk_level",
    size="risk_score",
    hover_data=["transformer_id", "age_years", "rainfall_mm"],
    title="Transformer Load vs Oil Temperature",
    labels={
        "load_percent": "Load (%)",
        "oil_temp_c": "Oil Temperature (°C)"
    }
)

st.plotly_chart(scatter_fig, use_container_width=True)


# Filters

st.sidebar.header("Filters")

# Risk Level filter
selected_risk = st.sidebar.selectbox(
    "Select Risk Level",
    options=["ALL", "HIGH", "MEDIUM", "LOW"]
)

filtered_data = data.copy()

# Transformer ID filter
transformer_ids = ["ALL"] + sorted(data["transformer_id"].unique().tolist())

selected_transformer = st.sidebar.selectbox(
    "Select Transformer ID",
    options=transformer_ids
)

if selected_transformer != "ALL":
    filtered_data = filtered_data[
        filtered_data["transformer_id"] == selected_transformer
    ]


if selected_risk != "ALL":
    filtered_data = filtered_data[filtered_data["risk_level"] == selected_risk]


st.subheader("Transformer Risk Overview")

def color_risk(val):
    if val == "HIGH":
        return "background-color: #ff4d4d; color: white;"
    elif val == "MEDIUM":
        return "background-color: #ffd966;"
    else:
        return "background-color: #7ddc7d;"
    
styled_df = filtered_data.style.applymap(color_risk, subset=["risk_level"])
st.dataframe(styled_df, use_container_width=True)
