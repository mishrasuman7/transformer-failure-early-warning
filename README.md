# ⚡ AI-Based Transformer Failure Early Warning System

## Overview
This project is an **engineering-focused system** designed to monitor operational parameters of electrical transformers and predict potential failure risks.

It combines:
- Traditional **rule-based engineering logic**
- **AI-based machine learning predictions**

The system helps engineers analyze transformer health, visualize risk patterns, and make informed preventive maintenance decisions.

---

## Key Objectives
- Early detection of transformer failure risks
- Comparison between rule-based and AI-based risk assessment
- Explainable AI outputs for engineering interpretation
- Interactive visualization of operational data

---

## Features
- Rule-based risk calculation using engineering thresholds
- AI-based failure risk prediction
- Risk confidence score
- Explainable AI risk reasons
- Interactive Streamlit dashboard
- CSV data upload support
- Toggle between Rule-Based and AI-Based risk modes
- KPIs, charts, and color-coded risk tables

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
└── venv/   (ignored in Git)
```

---

## Input Data Format
The input CSV file must contain the following columns:

```
transformer_id,load_percent,oil_temp_c,rainfall_mm,age_years
```

---

## Risk Calculation Modes

### 1. Rule-Based Mode
Risk is calculated using predefined engineering thresholds based on:
- Electrical load
- Oil temperature
- Rainfall / moisture exposure
- Transformer age

### 2. AI-Based Mode
A trained machine learning model predicts:
- Failure risk level
- Confidence score
- Risk explanation based on operational parameters

The mode can be switched using the sidebar toggle.

---

## How to Run the Project

### Clone the Repository
```
git clone <https://github.com/mishrasuman7/transformer-failure-early-warning.git>
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

### Run the Application
```
streamlit run app/main.py
```

---

## Visualizations
- Risk distribution bar charts
- Load vs Oil Temperature scatter plots
- Risk-level KPIs
- Filterable and color-coded data tables

---

## Future Enhancements
- Improve AI model accuracy and validation
- Automated model retraining
- Alert and notification system
- Backend API integration
- Database support for historical data
- Cloud deployment

---

## Engineering Use Case
This system can be used as a **decision-support tool** for:
- Transformer health monitoring
- Preventive maintenance planning
- Operational risk assessment
- Engineering analysis and research
