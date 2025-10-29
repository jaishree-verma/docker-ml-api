import streamlit as st
import requests

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

st.title("🌸 Iris Flower Classifier")
st.markdown("Enter the flower measurements below to predict its species using a trained ML model.")

sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

features = [sepal_length, sepal_width, petal_length, petal_width]

if st.button("Predict"):
    if all(f > 0 for f in features):
        try:
            response = requests.post(
                "https://docker-ml-api.onrender.com/predict",
                json={"features": features}
            )
            response.raise_for_status()
            prediction = response.json()["prediction"][0]
            species = ["Setosa", "Versicolor", "Virginica"][prediction]
            st.success(f"🌼 Predicted Species: **{species}** (Class {prediction})")
        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")
    else:
        st.warning("Please enter all four measurements greater than 0.")

st.markdown("---")
st.caption("Powered by FastAPI + Streamlit • Deployed with Render & Streamlit Cloud")
