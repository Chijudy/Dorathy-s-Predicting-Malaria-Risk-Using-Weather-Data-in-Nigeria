from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="Malaria Prediction API")

# Load model
model = joblib.load("malaria_model.pkl")

# Optional: load feature list
try:
    features = joblib.load("features.pkl")
except:
    features = [
        'rainfall_lag1', 'rainfall_lag2', 'rainfall_lag3',
        'temp_lag1', 'humidity_lag1',
        'rainfall_avg_3', 'temp_avg_3',
        'month_num', 'quarter'
    ]

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    
    # Ensure correct feature order
    df = df[features]
    
    prediction = model.predict(df)[0]

    # Risk classification
    if prediction > 500:
        risk = "High 🔴"
    elif prediction > 200:
        risk = "Medium 🟡"
    else:
        risk = "Low 🟢"

    return {
        "prediction": int(prediction),
        "risk": risk
    }