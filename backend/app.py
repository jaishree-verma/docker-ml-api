from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

app = FastAPI()

class Features(BaseModel):
    features: list[float]

model_path = "model.pkl"

if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))
else:
    model = None
    print("⚠️ model.pkl not found!")

@app.post("/predict")
def predict(data: Features):
    if model is None:
        return {"error": "Model not loaded"}
    prediction = model.predict([data.features])
    return {"prediction": prediction.tolist()}
