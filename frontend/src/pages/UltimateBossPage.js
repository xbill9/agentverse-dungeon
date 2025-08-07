import React, { useState, useEffect } from 'react';
import { useBackground } from '../contexts/BackgroundContext';

const UltimateBossPage = ({ onGameStart }) => {
    const [endpoints, setEndpoints] = useState({
        Shadowblade: 'http://localhost:8080/player-agent',
        Scholar: 'http://localhost:8080/player-agent',
        Guardian: 'http://localhost:8080/player-agent',
        Summoner: 'http://localhost:8080/player-agent',
    });
    const { setBackground } = useBackground();

    useEffect(() => {
        setBackground('/assets/images/bf-ultimate.png');
    }, [setBackground]);

    const handleStart = () => {
        onGameStart('ultimate', { a2a_endpoints: endpoints });
    };

    const handleChange = (playerClass, value) => {
        setEndpoints(prev => ({ ...prev, [playerClass]: value }));
    };

    return (
        <div className="main-menu">
            <h1>The Void's Maw</h1>
            <div className="menu-section">
                {Object.keys(endpoints).map(playerClass => (
                    <div className="form-group" key={playerClass}>
                        <label>{playerClass} A2A Endpoint:</label>
                        <input 
                            type="text" 
                            value={endpoints[playerClass]}
                            onChange={(e) => handleChange(playerClass, e.target.value)} 
                        />
                    </div>
                ))}
                <button className="btn btn-ultimate" onClick={handleStart}>Enter</button>
            </div>
        </div>
    );
};

export default UltimateBossPage;
