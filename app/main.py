import pandas as pd
import streamlit as st

# Page config

st.set_page_config(
    page_title="Transformer Early Warning",
    layout="wide"
)

st.title("AI-Based Transformer Failure Early Warning System")

# Risk logic

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

# Load data
data = pd.read_csv("data/sample_transformer_data.csv")
data["risk_score"] = data.apply(calculate_risk, axis=1)
data["risk_level"] = data["risk_score"].apply(risk_level)

# KPI SECTION

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


# Color styling
def color_risk(val):
    if val == "HIGH":
        return "background-color: #ff4d4d; color: white;"
    elif val == "MEDIUM":
        return "background-color: #ffd966;"
    else:
        return "background-color: #7ddc7d;"

styled_df = data.style.applymap(color_risk, subset=["risk_level"])

st.subheader("Transformer Risk Overview")
st.dataframe(styled_df, use_container_width=True)
