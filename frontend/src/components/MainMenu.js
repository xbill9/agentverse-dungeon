import React from 'react';
import { Link } from 'react-router-dom';

const MainMenu = () => {
  return (
    <div className="main-menu">
      <h1>Choose Your Battle</h1>
      <div className="menu-buttons">
        <Link to="/mini-boss">
          <button className="btn">Enter Mini Boss Dungeon</button>
        </Link>
        <Link to="/ultimate-boss">
          <button className="btn btn-ultimate">Enter The Void's Maw</button>
        </Link>
      </div>
    </div>
  );
};

export default MainMenu;
