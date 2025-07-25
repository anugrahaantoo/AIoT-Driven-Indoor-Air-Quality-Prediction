import React from 'react';

const WeatherCard = ({ temp, humidity }) => (
  <div className="weather-card">
    <h3>☀️ Weather Info</h3>
    <p>🌡️ Temperature: {temp}°C</p>
    <p>💧 Humidity: {humidity}%</p>
    <p>🌬️ Wind: 12 km/h</p>
    <p>🌞 UV Index: 8</p>
  </div>
);

export default WeatherCard;
