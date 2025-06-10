import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const icons = {
  Avocado: L.divIcon({ html: '🥑', iconSize: [30, 30], className: 'emoji-marker' }),
  Strawberry: L.divIcon({ html: '🍓', iconSize: [30, 30], className: 'emoji-marker' }),
  Blueberry: L.divIcon({ html: '🫐', iconSize: [30, 30], className: 'emoji-marker' })
};

const getIcon = type => icons[type] || icons.Avocado;

const MapView = ({ farms, selected }) => {
  const mapRef = useRef();

  useEffect(() => {
    if (selected && mapRef.current) {
      const map = mapRef.current;
      map.setView([selected.lat, selected.lng], 10);
    }
  }, [selected]);

  return (
    <MapContainer center={[-20.9176, 142.7028]} zoom={6} className="map" ref={mapRef}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" attribution="&copy; OpenStreetMap contributors" />
      {farms.map(farm => (
        <Marker key={farm.id} position={[farm.lat, farm.lng]} icon={getIcon(farm.type)}>
          <Popup>
            <strong>{farm.name}</strong><br />
            Region: {farm.region}<br />
            Type: {farm.type}<br />
            Area: {farm.area} ha<br />
            Established: {farm.established}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapView;
