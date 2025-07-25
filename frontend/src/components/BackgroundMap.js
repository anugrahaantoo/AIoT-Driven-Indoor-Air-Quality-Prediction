import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import './BackgroundMap.css';

const RecenterMap = ({ position }) => {
  const map = useMap();
  useEffect(() => {
    if (position) {
      map.setView(position, 12);
    }
  }, [position, map]);
  return null;
};

// Fix marker icons
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const BackgroundMap = () => {
  const [position, setPosition] = useState([25.276987, 55.296249]);
  const [locationText, setLocationText] = useState('Fetching location...'); // 🆕
  const [time, setTime] = useState(''); // 🆕

  useEffect(() => {
    const updateTime = () => {
      const now = new Date();
      setTime(now.toLocaleString());
    };
    updateTime();
    const interval = setInterval(updateTime, 60000); // every 1 min
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      async (pos) => {
        const { latitude, longitude } = pos.coords;
        setPosition([latitude, longitude]);

        // 🆕 Reverse Geocoding
        try {
          const response = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`);
          const data = await response.json();
          setLocationText(`${data.address.city || data.address.town || data.address.village || data.address.state || data.address.county}, ${data.address.country}`);
        } catch {
          setLocationText(`Lat: ${latitude.toFixed(2)}, Lon: ${longitude.toFixed(2)}`);
        }
      },
      () => {
        setLocationText("Location access denied");
      }
    );
  }, []);

  return (
  <div className="map-container-wrapper">
    <div className="location-time-banner">
      <h2>{locationText}</h2>
      <p><strong>Last Updated:</strong> {time}</p>
    </div>

    <MapContainer center={position} zoom={12} zoomControl={false} scrollWheelZoom={false}
  doubleClickZoom={false}
  dragging={false}
  keyboard={false} style={{ height: '70%', width: '100%' }} className="background-map">
      <TileLayer
        url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
        attribution="&copy; OpenStreetMap contributors, © Carto"
      />
      <Marker position={position}>
        <Popup>You are here</Popup>
      </Marker>
      <RecenterMap position={position} />
    </MapContainer>
  </div>
);

};

export default BackgroundMap;
