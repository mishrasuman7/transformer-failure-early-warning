from predict import predict_risk

# Example transformer input
sample_input = {
    "load_percent": 90,
    "oil_temp_c": 75,
    "rainfall_mm": 150,
    "age_years": 20
}

result = predict_risk(sample_input)

print("AI Prediction Result:")
print(result)
