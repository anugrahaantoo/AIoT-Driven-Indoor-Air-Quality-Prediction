import React from 'react';
import './AQIInputForm.css';

const AQIInputForm = ({ features, setFeatures, setResult }) => {
  const handleChange = async (e) => {
    const updatedFeatures = {
      ...features,
      [e.target.name]: parseFloat(e.target.value),
    };
    setFeatures(updatedFeatures);

    // Automatically call prediction API
    try {
      const res = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedFeatures),
      });
      const data = await res.json();
      setResult(data.prediction);
    } catch (error) {
      console.error("Prediction fetch failed", error);
    }
  };

  return (
    <div className="aqi-input-form">
      <h3>Indoor AQI</h3>
      <table className="aqi-input-table">
        <tbody>
          {[
            ['PM2.5', 'PM2.5', 'µg/m³'],
            ['CO', 'CO_mgm3', 'ppb'],
            ['NO2', 'NO2_ugm3', 'ppb'],
            ['NH3', 'NH3_ugm3', 'ppb'],
            ['O3', 'O3_ugm3', 'ppb'],
            ['Temp (°C)', 'Temp', '°C'],
            ['Humidity (%)', 'Humidity', '%'],
            ['Pressure (hPa)', 'Pressure', 'hPa'],
          ].map(([label, name, unit]) => (
            <tr key={name}>
              <td className="label-cell">{label}</td>
              <td>
                <input
                  type="number"
                  name={name}
                  value={features[name]}
                  onChange={handleChange}
                  step="0.1"
                  required
                  className="input-cell"
                />
              </td>
              <td className="unit-cell">{unit}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AQIInputForm;
