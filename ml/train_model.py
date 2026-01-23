#Training Scripts
import pandas as pd

# Load data
# "data" / "sample_transformer_data.csv"
data = pd.read_csv("data/sample_transformer_data.csv")


# Create labels (target)
def create_label(row):
    # High-risk condition (engineering-based)
    if (
        row["load_percent"] > 85 and
        row["oil_temp_c"] > 70 and
        row["age_years"] > 15
    ):
        return 1  # High failure risk
    else:
        return 0  # Normal

data["failure_risk"] = data.apply(create_label, axis=1)

print(data)
