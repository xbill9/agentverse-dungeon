import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useBackground } from '../contexts/BackgroundContext';
const HomePage = () => {
  const { setBackground } = useBackground();

  useEffect(() => {
    setBackground('/assets/images/homepage.png');
  }, [setBackground]);

  return (
    <div className="main-menu">
      <h1>Choose Your Battle</h1>
      <div className="menu-buttons">
        <Link to="/mini-boss">
          <button className="btn">Enter The Crimson Keep</button>
        </Link>
        <Link to="/ultimate-boss">
          <button className="btn btn-ultimate" disabled>Enter The Void's Maw</button>
        </Link>
      </div>
    </div>
  );
};

export default HomePage;