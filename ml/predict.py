import joblib
import pandas as pd
from pathlib import Path

# Resolve paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml" / "model.pkl"

# Load model ONCE
model = joblib.load(MODEL_PATH)

FEATURES = [
    "load_percent",
    "oil_temp_c",
    "rainfall_mm",
    "age_years"
]

def predict_risk(input_data: dict):
    """
    input_data example:
    {
        "load_percent": 85,
        "oil_temp_c": 72,
        "rainfall_mm": 120,
        "age_years": 18
    }
    """
    df = pd.DataFrame([input_data], columns=FEATURES)
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "risk_label": int(prediction),
        "risk_probability": round(float(probability), 2)
    }
