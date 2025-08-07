
import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => (
  <div className="main-menu">
    <h1>Choose Your Battle</h1>
    <div className="menu-buttons">
      <Link to="/mini-boss">
        <button>Enter Mini Boss Dungeon</button>
      </Link>
      <Link to="/final-boss">
        <button>Enter Final Boss</button>
      </Link>
      <Link to="/ultimate-boss">
        <button>Enter The Void's Maw</button>
      </Link>
    </div>
  </div>
);

export default HomePage;
