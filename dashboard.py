import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
from shap import TreeExplainer, Explanation

# ---------------------------
# Setup and Load Dependencies
# ---------------------------
st.set_page_config(page_title="Indoor Air Quality Prediction", layout="centered")
st.title("🌬️ Indoor Air Quality (EAQI) Prediction Dashboard")
st.markdown("This dashboard predicts **EAQI categories** using indoor pollutant levels and environmental conditions.")

# Load label encoder
label_encoder = joblib.load("notebooks/label_encoder.pkl")

# Available model pipelines
model_paths = {
    "CatBoost": "notebooks/trained_models/CatBoost.pkl",
    "XGBoost": "notebooks/trained_models/XGBoost.pkl",
    "LightGBM": "notebooks/trained_models/LightGBM.pkl",
    "Gradient Boosting": "notebooks/trained_models/Gradient_Boosting.pkl",
    "Random Forest": "notebooks/trained_models/Random_Forest.pkl",
    "Linear SVM": "notebooks/trained_models/Linear_SVM.pkl",
    "Logistic Regression": "notebooks/trained_models/Logistic_Regression.pkl",
    "MLP Classifier": "notebooks/trained_models/MLP_Classifier.pkl",
    "Naive Bayes": "notebooks/trained_models/Naive_Bayes.pkl",
    "Nearest Centroid": "notebooks/trained_models/Nearest_Centroid.pkl",
    "Ridge_Classifier": "notebooks/trained_models/Ridge_Classifier.pkl"
}

# ------------------
# Sidebar User Input
# ------------------
st.sidebar.header("Enter Input Features")
PM = st.sidebar.slider("PM2.5 (µg/m³)", 0.0, 2000.0, 75.0)
CO = st.sidebar.slider("CO (µg/m³)", 0.0, 58400.0, 10.0)
NO2 = st.sidebar.slider("NO₂ (µg/m³)", 0.0, 3853.0, 20.0)
NH3 = st.sidebar.slider("NH₃ (µg/m³)", 0.0, 300.0, 30.0)
O3 = st.sidebar.slider("O₃ (µg/m³)", 0.0, 2350.0, 60.0)
Temp = st.sidebar.slider("Temperature (°C)", 0.0, 50.0, 25.0)
Humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 50.0)
Pressure = st.sidebar.slider("Pressure (hPa)", 900.0, 1100.0, 1013.0)

# Assemble user input
input_df = pd.DataFrame([[PM, CO, NO2, NH3, O3, Temp, Humidity, Pressure]],
                        columns=['PM2.5', 'CO_mgm3', 'NO2_ugm3', 'NH3_ugm3', 'O3_ugm3', 'Temp', 'Humidity', 'Pressure']
)

# ------------------------------
# Multi-model Prediction Display
# ------------------------------
st.subheader("🤖 Predictions from All Models")

prediction_results = {}
pipelines = {}

for name, path in model_paths.items():
    try:
        pipe = joblib.load(path)
        pipelines[name] = pipe  # Save for optional SHAP
        pred = pipe.predict(input_df)[0]
        pred_label = label_encoder.inverse_transform([pred])[0]
        prediction_results[name] = pred_label
    except Exception as e:
        prediction_results[name] = f"❌ Error {str(e)}"

# Show in table
results_df = pd.DataFrame.from_dict(prediction_results, orient='index', columns=['Predicted EAQI'])
st.table(results_df)


