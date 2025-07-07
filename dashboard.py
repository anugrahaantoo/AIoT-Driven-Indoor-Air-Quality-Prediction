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
label_encoder = joblib.load("label_encoder04.pkl")

# Available model pipelines
model_paths = {
    "CatBoost": "trained_models/CatBoost.pkl",
    "XGBoost": "trained_models/XGBoost.pkl",
    "LightGBM": "trained_models/LightGBM.pkl",
    "Gradient Boosting": "trained_models/Gradient_Boosting.pkl",
    "Random Forest": "trained_models/Random_Forest.pkl"
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
                        columns=['PM2.5', 'CO_ugm3', 'NO2_ugm3', 'NH3_ugm3', 'O3_ugm3', 'Temp', 'Humidity', 'Pressure'])

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
        prediction_results[name] = f"❌ Error"

# Show in table
results_df = pd.DataFrame.from_dict(prediction_results, orient='index', columns=['Predicted EAQI'])
st.table(results_df)

# -----------------------------
# Optional SHAP for 1 Model
# -----------------------------
st.subheader("📊 SHAP Explanation for Selected Model")
selected_model_name = st.selectbox("Choose model for SHAP", list(pipelines.keys()))
try:
    model_pipeline = pipelines[selected_model_name]
    model = model_pipeline.named_steps['clf']
    X_scaled = model_pipeline.named_steps['scaler'].transform(input_df)

    explainer = TreeExplainer(model)
    shap_values = explainer.shap_values(X_scaled)

    # Handle multiclass SHAP values
    class_idx = model_pipeline.predict(input_df)[0]
    base_val = explainer.expected_value[class_idx] if isinstance(explainer.expected_value, list) else explainer.expected_value
    shap_val = shap_values[class_idx][0] if isinstance(shap_values, list) else shap_values[0]

    st.set_option('deprecation.showPyplotGlobalUse', False)
    shap.plots.waterfall(Explanation(
        values=shap_val,
        base_values=base_val,
        data=X_scaled[0],
        feature_names=input_df.columns.tolist()
    ), max_display=8)
    st.pyplot(bbox_inches='tight', dpi=300, pad_inches=0)

except Exception as e:
    st.error(f"⚠️ SHAP explanation failed: {e}")

# -------------------------
# CSV Batch Prediction Area
# -------------------------
st.subheader("📥 Upload CSV for Batch Prediction")
csv_file = st.file_uploader("Upload a CSV file with the same 8 input columns", type=["csv"])
if csv_file:
    try:
        batch_df = pd.read_csv(csv_file)
        expected_cols = ['PM2.5', 'CO_ugm3', 'NO2_ugm3', 'NH3_ugm3', 'O3_ugm3', 'Temp', 'Humidity', 'Pressure']
        if set(batch_df.columns) != set(expected_cols):
            st.error("❌ Uploaded CSV must contain the correct 8 feature columns.")
        else:
            best_model_name = "Gradient Boosting"  # or use dropdown
            model_pipeline = pipelines[best_model_name]
            preds = model_pipeline.predict(batch_df)
            batch_df['Predicted_EAQI'] = label_encoder.inverse_transform(preds)

            st.write(batch_df.head())
            st.download_button("📥 Download Results", batch_df.to_csv(index=False), "predicted_eaqi.csv", "text/csv")

            # Show distribution
            st.subheader("📈 EAQI Prediction Distribution")
            st.bar_chart(batch_df['Predicted_EAQI'].value_counts())

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
