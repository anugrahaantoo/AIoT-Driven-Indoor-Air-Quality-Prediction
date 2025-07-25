from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os

predict_bp = Blueprint('predict', __name__)

model_path = os.path.join('trained_models', 'XGBoost.pkl')
label_path = 'label_encoder.pkl'

model = joblib.load(model_path)
label_encoder = joblib.load(label_path)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([
        data['PM2.5'],
        data['CO_mgm3'],
        data['NO2_ugm3'],
        data['NH3_ugm3'],
        data['O3_ugm3'],
        data['Temp'],
        data['Humidity'],
        data['Pressure']
    ]).reshape(1, -1)

    prediction = model.predict(features)[0]
    label = label_encoder.inverse_transform([prediction])[0]

    return jsonify({'prediction': label})
