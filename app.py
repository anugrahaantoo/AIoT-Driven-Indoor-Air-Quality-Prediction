import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and feature columns
model = joblib.load("best_model_pipeline02.pkl")  # Save your trained model as this
feature_names = joblib.load("feature_names.pkl")  # Save your X.columns as this

st.title("Indoor Air Quality (EAQI) Predictor 🌬️")
st.markdown("Enter pollutant and weather values below to predict indoor air quality level.")

# Create input fields
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}", step=0.01)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Predict button
if st.button("Predict EAQI Category"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted EAQI Level: **{prediction}**")
