"""
Health bill prediction API.

1. Train the model first:   python ../../model/regression.py
2. Run the API:             uvicorn app:app --reload
3. Open the docs:           http://127.0.0.1:8000/docs
"""

import pickle
from pathlib import Path
from typing import Literal

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_DIR = Path(__file__).resolve().parents[2] / "model"

# Load the model and transformer
with open(MODEL_DIR / "linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)
with open(MODEL_DIR / "transformer.pkl", "rb") as f:
    transformer = pickle.load(f)

app = FastAPI(title="Health Bill Prediction")


# Pydantic validates the request, so missing or invalid fields return HTTP 422
class HealthData(BaseModel):
    age: int = Field(..., ge=0, le=120)
    gender: Literal["Male", "Female"]
    blood_type: Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    medical_condition: Literal[
        "Arthritis", "Asthma", "Cancer", "Diabetes", "Hypertension", "Obesity"
    ]


@app.post("/predict/")
def predict(data: HealthData):
    input_df = pd.DataFrame([{
        "Age": data.age,
        "Gender": data.gender,
        "Blood Type": data.blood_type,
        "Medical Condition": data.medical_condition,
    }])

    transformed_features = transformer.transform(input_df)
    prediction = model.predict(transformed_features)
    # Convert numpy float to a plain Python float so it serializes to JSON
    return {"Predicted Billing Amount": round(float(prediction[0]), 2)}
