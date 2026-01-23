import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib


# Resolve paths

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "sample_transformer_data.csv"
MODEL_PATH = BASE_DIR / "ml" / "model.pkl"


# Load raw data

data = pd.read_csv(DATA_PATH)


# Create labels 

def create_label(row):
    if (
        row["load_percent"] > 85 and
        row["oil_temp_c"] > 70 and
        row["age_years"] > 15
    ):
        return 1
    return 0

data["failure_risk"] = data.apply(create_label, axis=1)


# Features and target

FEATURES = [
    "load_percent",
    "oil_temp_c",
    "rainfall_mm",
    "age_years"
]

X = data[FEATURES]
y = data["failure_risk"]


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# Evaluate

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Save model

joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
