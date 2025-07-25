import React, { useState } from 'react';
import AQIInputForm from '../components/AQIInputForm';
import PredictionResult from '../components/PredictionResult';
import BackgroundMap from '../components/BackgroundMap';
import '../styles/dashboard.css';

const Dashboard = () => {
  const [result, setResult] = useState(null);
  const [features, setFeatures] = useState({
  'PM2.5': 47,
  'CO_mgm3': 10,
  'NO2_ugm3': 20,
  'NH3_ugm3': 30,
  'O3_ugm3': 60,
  'Temp': 38,
  'Humidity': 54,
  'Pressure': 1013
});

  return (
    <div className="dashboard-container">
  <div className="top-half">
    <BackgroundMap />
    <div className="centered-form">
      <AQIInputForm features={features} setFeatures={setFeatures} setResult={setResult} />
    </div>
  </div>

  <div className="bottom-half">
    <div className="result-section">
      <PredictionResult result={result} />
      <p className="disclaimer">
        *This prediction is based on indoor pollutant levels and is for informational purposes only.
      </p>
    </div>
  </div>
</div>


  );
};

export default Dashboard;
