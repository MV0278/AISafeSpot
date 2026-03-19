from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# load trained model
model = pickle.load(open("../model/safety_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "AI SafeSpot API running"}

@app.post("/predict")
def predict(rape:int, kidnapping:int, dowry:int, assault:int, minor:int, dv:int, trafficking:int):

    features = np.array([[rape, kidnapping, dowry, assault, minor, dv, trafficking]])

    prediction = model.predict(features)[0]

    return {"risk_score": float(prediction)}