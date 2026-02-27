import streamlit as st
import os
print(os.listdir())

from src.ingestion import load_claims
from src.feature_engineering import create_features
from src.anomaly_model import train_model, load_model, predict
from src.risk_scoring import calculate_risk
from src.report_generator import generate_report

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "assets", "pmjay_logo.jpeg")

st.image(logo_path, width=250)
st.title("🏥 Ayushman Bharat Fraud Detection Agent")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "raw", "claims.csv")

df = load_claims(file_path)

df = create_features(df)

model = train_model(df)
df = predict(model, df)

df = calculate_risk(df)

st.subheader("📊 Fraud Detection Dashboard")
st.dataframe(df.head())

st.subheader("🚨 High Risk Claims")
st.dataframe(df[df["risk_level"] == "High"])

report = generate_report(df)

st.subheader("📄 Risk Report")
st.text(report)