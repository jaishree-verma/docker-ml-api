import streamlit as st
import requests

st.set_page_config(page_title="Iris Classifier", page_icon="🌸")
st.title("🌸 Iris Flower Classifier")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

features = [sepal_length, sepal_width, petal_length, petal_width]

if st.button("Predict"):
    try:
        response = requests.post("http://backend:5000/predict", json={"features": features})
        prediction = response.json()["prediction"][0]
        species = ["Setosa", "Versicolor", "Virginica"][prediction]
        st.success(f"🌼 Predicted Species: **{species}** (Class {prediction})")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
