import streamlit as st
import joblib
import numpy as np

# load model (FIXED PATH)
model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction App")

area = st.number_input("Enter Area (sqft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms]])
    
    prediction = model.predict(features)

    st.success(f"🏠 Predicted Price: ₹ {prediction[0]}")