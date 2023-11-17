import streamlit as st
import pandas as pd
import pickle

# Load both the model and the transformer
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
transformer = pickle.load(open('transformer.pkl', 'rb'))


st.title('Health Bill Prediction')

age = st.number_input('Age', min_value=1, step=1)
gender = st.selectbox('Gender', options=['Male', 'Female'])
blood_type = st.selectbox('Blood Type', options=['A', 'B', 'AB', 'O'])
medical_condition = st.text_input('Medical Condition')

input_df = pd.DataFrame([{
    'Age': age,
    'Gender': gender,
    'Blood Type': blood_type,
    'Medical Condition': medical_condition
}])

if st.button('Predict'):
    if input_df.isnull().values.any():
        st.error('Please fill in all required fields.')
    else:
        transformed_features = transformer.transform(input_df)
        prediction = model.predict(transformed_features)
        output = round(prediction[0], 2)
        st.success(f'Predicted Billing Amount is {output}')
