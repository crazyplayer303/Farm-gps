import React, { useEffect, useState } from 'react';
import FarmList from './components/FarmList';
import FarmStats from './components/FarmStats';
import MapView from './components/MapView';

const App = () => {
  const [farms, setFarms] = useState([]);
  const [search, setSearch] = useState('');
  const [type, setType] = useState('');
  const [selectedFarm, setSelectedFarm] = useState(null);

  useEffect(() => {
    const params = new URLSearchParams();
    if (search) params.append('search', search);
    if (type) params.append('type', type);
    fetch('/api/farms?' + params.toString())
      .then(res => res.json())
      .then(data => {
        setFarms(data.items || []);
      })
      .catch(err => console.error('Failed to load farms', err));
  }, [search, type]);

  return (
    <div className="container">
      <div className="header">
        <h1>Farm GPS</h1>
      </div>
      <div className="controls">
        <input
          type="text"
          placeholder="Search farms..."
          value={search}
          onChange={e => setSearch(e.target.value)}
        />
        <select value={type} onChange={e => setType(e.target.value)}>
          <option value="">All farm types</option>
          <option value="Avocado">Avocado</option>
          <option value="Strawberry">Strawberry</option>
          <option value="Blueberry">Blueberry</option>
        </select>
      </div>
      <FarmStats farms={farms} />
      <div className="main">
        <div className="farm-list">
          <FarmList farms={farms} onSelect={setSelectedFarm} />
        </div>
        <MapView farms={farms} selected={selectedFarm} />
      </div>
    </div>
  );
};

export default App;
