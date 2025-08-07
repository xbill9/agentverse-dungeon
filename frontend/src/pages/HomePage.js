import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => (
  <div className="main-menu">
    <h1>Choose Your Battle</h1>
    <div className="menu-buttons">
      <Link to="/mini-boss">
        <button>Enter The Crimson Keep</button>
      </Link>
      <Link to="/ultimate-boss">
        <button>Enter The Void's Maw</button>
      </Link>
    </div>
  </div>
);

export default HomePage;