# ⚡ AI-Based Transformer Failure Early Warning System

## Overview
AI-powered system to predict transformer failure risk using both rule-based logic and machine learning.
Built as a **job-prep / portfolio project** for a Full-Stack Software & AI Engineer role.

---

## Features
- Rule-based risk calculation
- AI-based risk prediction
- Confidence score for AI output
- Explainable AI reasons
- Streamlit dashboard
- CSV upload support
- Risk mode toggle (Rule-Based / AI-Based)
- Charts, KPIs, and color-coded tables

---

## Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- Scikit-learn
- Git & GitHub

---

## Project Structure

```
transformer-failure-early-warning/
├── app/
│   └── main.py
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   └── test_predict.py
├── data/
│   └── sample_transformer_data.csv
├── requirements.txt
├── README.md
└── venv/  (not committed)
```

---

## Input Data Format
CSV must contain the following columns:

```
transformer_id,load_percent,oil_temp_c,rainfall_mm,age_years
```

---

## How to Run

### Clone Repository
```
git clone <repo-url>
cd transformer-failure-early-warning
```

### Create & Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run Application
```
streamlit run app/main.py
```

---

## Risk Modes
- **Rule-Based** – Engineering thresholds
- **AI-Based** – Machine learning predictions with confidence

Switch modes using the sidebar toggle.

---

## Future Improvements
- Improve ML accuracy & evaluation
- Model retraining pipeline
- FastAPI backend
- Database integration
- Authentication
- Cloud deployment

---

## Purpose
This project demonstrates **real-world AI + full-stack integration**, explainability, and clean engineering practices for interviews and job preparation.
