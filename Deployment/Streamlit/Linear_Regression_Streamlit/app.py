"""
Health bill prediction app.

1. Train the model first:   python ../../model/regression.py
2. Run the app:             streamlit run app.py
"""

import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

MODEL_DIR = Path(__file__).resolve().parents[2] / "model"

# Load both the model and the transformer
with open(MODEL_DIR / "linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)
with open(MODEL_DIR / "transformer.pkl", "rb") as f:
    transformer = pickle.load(f)

st.title("Health Bill Prediction")

# Options match the categories in the training data
age = st.number_input("Age", min_value=1, max_value=120, step=1)
gender = st.selectbox("Gender", options=["Male", "Female"])
blood_type = st.selectbox(
    "Blood Type", options=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
)
medical_condition = st.selectbox(
    "Medical Condition",
    options=["Arthritis", "Asthma", "Cancer", "Diabetes", "Hypertension", "Obesity"],
)

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Blood Type": blood_type,
        "Medical Condition": medical_condition,
    }])
    transformed_features = transformer.transform(input_df)
    prediction = model.predict(transformed_features)
    st.success(f"Predicted Billing Amount is {round(float(prediction[0]), 2)}")
