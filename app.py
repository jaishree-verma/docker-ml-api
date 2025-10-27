# This serves as an inferemce APi which means here we can load or train model through web endpoints to serve predictions 
from fastapi import FastAPI, Request
import pickle

app = FastAPI()
model = pickle.load(open("model.pkl", "rb"))

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    prediction = model.predict([data["features"]])
    return {"prediction": prediction.tolist()}
