import streamlit as st
import pandas as pd
import requests

st.title('RetailIQ Demand Forecasting')

# User inputs
feature_1 = st.number_input('Feature 1')
feature_2 = st.number_input('Feature 2')
# ... Add more features as needed

# Prediction button
if st.button('Predict Demand'):
    data = {
        'feature_1': feature_1,
        'feature_2': feature_2,
        # ... Add more features
    }
    response = requests.post('http://localhost:80/predict', json=data)
    prediction = response.json()['prediction']
    st.write(f'Predicted Demand: {prediction}')
