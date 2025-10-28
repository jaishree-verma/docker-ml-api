# This serves as an inference API to load a trained model and serve predictions via web endpoints
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to ["http://localhost:5173"] if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Define input schema using Pydantic
class Features(BaseModel):
    features: list[float]

# Prediction endpoint
@app.post("/predict")
async def predict(input: Features):
    try:
        prediction = model.predict([input.features])
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
