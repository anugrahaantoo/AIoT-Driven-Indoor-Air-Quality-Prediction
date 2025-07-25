import React from 'react';
import './PredictionResult.css';

const PredictionResult = ({ result }) => {
  if (!result || typeof result !== 'string') return null;

  const label = result.trim().toLowerCase();

  const descriptions = {
    "good": "Indicates that the air quality is considered satisfactory and the air pollution concentrations pose no risk for the population.",
    "moderate": "The air quality is acceptable. However, there may be a moderate health concern for a very small number of unusually sensitive people.",
    "unhealthy for sensitive groups": "Serves as a warning so that sensitive individuals can take appropriate ‘exposure avoidance’ behaviour.",
    "unhealthy": "Exposure is associated with an increase in effects for the general public, especially sensitive groups.",
    "very unhealthy": "Everyone may experience more serious health effects. Health alerts are triggered at this level.",
    "hazardous": "The entire population is expected to be affected. Emergency warnings for health conditions are issued at this level.",
  };

  const displayLabel = label
    .split(' ')
    .map(word => word[0].toUpperCase() + word.slice(1))
    .join(' ');

  const cssClass = label.replace(/\s+/g, '-'); // e.g., 'unhealthy-for-sensitive-groups'

  return (
    <div className={`prediction-banner ${cssClass}`}>
      <h3>Air Quality is</h3>
      <div className="prediction-box">
        <span>{displayLabel}</span>
      </div>
      <p className="description">{descriptions[label] || "No information available."}</p>
    </div>
  );
};

export default PredictionResult;
