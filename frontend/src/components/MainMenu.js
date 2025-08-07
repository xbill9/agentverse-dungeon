import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

const MainMenu = ({ onGameStart }) => {
    const [config, setConfig] = useState(null);
    const [miniBossState, setMiniBossState] = useState({
        playerClass: 'Shadowblade',
        bossName: 'Procrastination',
        a2aEndpoint: 'http://localhost:8080/player-agent-mini'
    });

    const [ultimateBossState, setUltimateBossState] = useState({
        a2a_endpoints: {
            Shadowblade: 'http://localhost:8080/shadowblade',
            Scholar: 'http://localhost:8080/scholar',
            Guardian: 'http://localhost:8080/guardian',
            Summoner: 'http://localhost:8080/summoner',
        }
    });

    useEffect(() => {
        const fetchConfig = async () => {
            try {
                const response = await axios.get(`${API_URL}/api/config`);
                setConfig(response.data);
            } catch (err) {
                console.error('Could not fetch game configuration.');
            }
        };
        fetchConfig();
    }, []);

    const handleMiniBossChange = (e) => {
        const { name, value } = e.target;
        setMiniBossState(prev => ({ ...prev, [name]: value }));
    };

    const handleUltimateBossChange = (e) => {
        const { name, value } = e.target;
        setUltimateBossState(prev => ({
            a2a_endpoints: {
                ...prev.a2a_endpoints,
                [name]: value
            }
        }));
    };

    const handleMiniBossSubmit = (e) => {
        e.preventDefault();
        onGameStart('mini', {
            player_class: miniBossState.playerClass,
            boss_name: miniBossState.bossName,
            a2a_endpoint: miniBossState.a2aEndpoint,
        });
    };

    const handleUltimateBossSubmit = (e) => {
        e.preventDefault();
        onGameStart('ultimate', ultimateBossState);
    };

    const ultimateClasses = ["Shadowblade", "Scholar", "Guardian", "Summoner"];

    if (!config) {
        return <div>Loading configuration...</div>;
    }

    return (
        <div className="main-menu">
            <h1>Boss Fight Dungeon</h1>
            
            <div className="menu-section">
                <h2>Enter Mini-Boss Dungeon</h2>
                <form onSubmit={handleMiniBossSubmit}>
                    <div className="form-group">
                        <label htmlFor="playerClass">Choose Your Class:</label>
                        <select id="playerClass" name="playerClass" value={miniBossState.playerClass} onChange={handleMiniBossChange}>
                            {Object.keys(config.player_hp).filter(p => p !== "The Monolith of Managerial Oversight").map(pClass => <option key={pClass} value={pClass}>{pClass}</option>)}
                        </select>
                    </div>
                    <div className="form-group">
                        <label htmlFor="bossName">Choose Your Opponent:</label>
                        <select id="bossName" name="bossName" value={miniBossState.bossName} onChange={handleMiniBossChange}>
                             {Object.keys(config.boss_hp).filter(b => b !== "The Monolith of Managerial Oversight").map(bName => <option key={bName} value={bName}>{bName}</option>)}
                        </select>
                    </div>
                    <div className="form-group">
                        <label htmlFor="a2aEndpoint">Your A2A Endpoint:</label>
                        <input id="a2aEndpoint" name="a2aEndpoint" type="text" value={miniBossState.a2aEndpoint} onChange={handleMiniBossChange} />
                    </div>
                    <button type="submit" className="btn">Start Mini-Boss Fight</button>
                </form>
            </div>

            <div className="menu-section">
                <h2>Face the Ultimate Boss</h2>
                <form onSubmit={handleUltimateBossSubmit}>
                    {ultimateClasses.map(pClass => (
                        <div className="form-group" key={pClass}>
                            <label htmlFor={`a2a-${pClass}`}>{pClass} A2A Endpoint:</label>
                            <input 
                                id={`a2a-${pClass}`}
                                name={pClass}
                                type="text" 
                                value={ultimateBossState.a2a_endpoints[pClass]} 
                                onChange={handleUltimateBossChange} 
                            />
                        </div>
                    ))}
                    <button type="submit" className="btn btn-ultimate">Start Ultimate Boss Fight</button>
                </form>
            </div>
        </div>
    );
};

export default MainMenu;
