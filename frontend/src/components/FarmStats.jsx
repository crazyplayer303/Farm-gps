import React from 'react';

const FarmStats = ({ farms }) => {
  const totalFarms = farms.length;
  const totalArea = farms.reduce((sum, f) => sum + (f.area || 0), 0);
  const avgSize = totalFarms ? Math.round(totalArea / totalFarms) : 0;

  return (
    <div className="stats">
      <div className="stat-box">
        <div className="stat-number">{totalFarms}</div>
        <div>Total Farms</div>
      </div>
      <div className="stat-box">
        <div className="stat-number">{totalArea}</div>
        <div>Total Area (ha)</div>
      </div>
      <div className="stat-box">
        <div className="stat-number">{avgSize}</div>
        <div>Avg Size (ha)</div>
      </div>
    </div>
  );
};

export default FarmStats;
