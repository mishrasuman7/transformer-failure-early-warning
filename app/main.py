import pandas as pd
import streamlit as st

st.set_page_config(page_title="Transformer Early Warning", layout="wide")
st.title("AI-Based Transformer Failure Early Warning System")

data = pd.read_csv(
    r"E:\transformer-failure-early-warning\data\sample_transformer_data.csv"
)
# data = pd.read_csv("../data/sample_transformer_data.csv")

st.subheader("Transformer Monitoring Data")
st.dataframe(data)

