from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Load the model and transformer
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
transformer = pickle.load(open('transformer.pkl', 'rb'))

app = FastAPI()

# Define a Pydantic model for your data
class HealthData(BaseModel):
    age: int
    gender: str
    blood_type: str
    medical_condition: str

@app.post("/predict/")
async def predict(data: HealthData):
    # Convert the data to a DataFrame
    input_df = pd.DataFrame([{
        'Age': data.age,
        'Gender': data.gender,
        'Blood Type': data.blood_type,
        'Medical Condition': data.medical_condition
    }])

    # Check for missing values
    if input_df.isnull().values.any():
        return {"error": "Please fill in all required fields."}
    else:
        # Transform and predict
        transformed_features = transformer.transform(input_df)
        prediction = model.predict(transformed_features)
        output = round(prediction[0], 2)
        return {"Predicted Billing Amount": output}

# The app will be run using a command like: uvicorn app:app --reload
