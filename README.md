# 🚀 Dockerized ML Model API with FastAPI

This project demonstrates how to train a machine learning model using scikit-learn, serve predictions via a FastAPI endpoint, and containerize the entire app using Docker. It’s a clean, minimal setup perfect for learning how to deploy ML models as APIs.


---

## 🧪 How to Run Locally

### 1. Train the model
```bash
python train_model.py
docker build -t ml-api .
docker run -p 5000:5000 ml-api
Invoke-RestMethod -Uri http://localhost:5000/predict `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"features": [5.1, 3.5, 1.4, 0.2]}'
pip install -r requirements.txt
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
