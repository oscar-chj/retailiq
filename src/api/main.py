from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('models/best_random_forest_model.pkl')

@app.post('/predict')
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {'prediction': prediction[0]}
