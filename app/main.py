import pandas as pd
import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Transformer Early Warning",
    layout="wide"
)

st.title("AI-Based Transformer Failure Early Warning System")

# ----------------------------
# Risk calculation logic
# ----------------------------
def calculate_risk(row):
    risk = 0

    # Load impact
    if row["load_percent"] > 80:
        risk += 30
    elif row["load_percent"] > 60:
        risk += 15

    # Temperature impact
    if row["oil_temp_c"] > 70:
        risk += 30
    elif row["oil_temp_c"] > 55:
        risk += 15

    # Rainfall impact
    if row["rainfall_mm"] > 20:
        risk += 20
    elif row["rainfall_mm"] > 5:
        risk += 10

    # Age impact
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


# ----------------------------
# Load data
# ----------------------------
data = pd.read_csv("data/sample_transformer_data.csv")

# ----------------------------
# Apply risk logic
# ----------------------------
data["risk_score"] = data.apply(calculate_risk, axis=1)
data["risk_level"] = data["risk_score"].apply(risk_level)

# ----------------------------
# Display
# ----------------------------
st.subheader("Transformer Risk Status")
st.dataframe(data)
