import React from 'react';

const FarmList = ({ farms, onSelect }) => {
  return (
    <div>
      {farms.map(farm => (
        <div key={farm.id} className="farm-item" onClick={() => onSelect(farm)}>
          <strong>{farm.name}</strong> - {farm.type || 'Unknown'} in {farm.region} ({farm.area} ha)
        </div>
      ))}
    </div>
  );
};

export default FarmList;
