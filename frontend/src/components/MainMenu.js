import React from 'react';

const MainMenu = ({ setPage }) => {
  return (
    <div className="main-menu">
      <h1>Choose Your Battle</h1>
      <div className="menu-buttons">
        <button className="btn" onClick={() => setPage('mini-boss')}>Enter Mini Boss Dungeon</button>
        <button className="btn btn-ultimate" onClick={() => setPage('ultimate-boss')}>Enter The Void's Maw</button>
      </div>
    </div>
  );
};

export default MainMenu;
