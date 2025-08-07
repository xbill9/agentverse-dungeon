import React, { useState, useEffect } from 'react';
import { useBackground } from '../contexts/BackgroundContext';

const MiniBossPage = ({ onGameStart }) => {
    const [playerClass, setPlayerClass] = useState('Shadowblade');
    const [boss, setBoss] = useState('Procrastination');
    const [a2aEndpoint, setA2aEndpoint] = useState('http://localhost:8080/player-agent');
    const { setBackground } = useBackground();

    useEffect(() => {
        setBackground('/assets/images/enterinfo.png');
    }, [setBackground]);

    const handleStart = () => {
        onGameStart('mini', { player_class: playerClass, boss_name: boss, a2a_endpoint: a2aEndpoint });
    };

    return (
        <div className="main-menu">
            <h1>Mini Boss Dungeon</h1>
            <div className="menu-section">
                <div className="form-group">
                    <label>Choose Your Class:</label>
                    <select value={playerClass} onChange={(e) => setPlayerClass(e.target.value)}>
                        <option value="Shadowblade">Shadowblade</option>
                        <option value="Scholar">Scholar</option>
                        <option value="Guardian">Guardian</option>
                        <option value="Summoner">Summoner</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>Choose Your Boss:</label>
                    <select value={boss} onChange={(e) => setBoss(e.target.value)}>
                        <option value="Procrastination">Procrastination</option>
                        <option value="Hype">Hype</option>
                        <option value="Dogma">Dogma</option>
                        <option value="Legacy">Legacy</option>
                        <option value="Perfectionism">Perfectionism</option>
                        <option value="Obfuscation">Obfuscation</option>
                        <option value="Apathy">Apathy</option>
                    </select>
                </div>
                <div className="form-group">
                    <label>A2A Endpoint:</label>
                    <input type="text" value={a2aEndpoint} onChange={(e) => setA2aEndpoint(e.target.value)} />
                </div>
                <button className="btn" onClick={handleStart}>Enter</button>
            </div>
        </div>
    );
};

export default MiniBossPage;