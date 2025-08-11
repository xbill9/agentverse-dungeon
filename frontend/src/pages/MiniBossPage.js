import React, { useState, useEffect } from 'react';
import { useBackground } from '../contexts/BackgroundContext';

const MiniBossPage = ({ onGameStart }) => {
    const [playerClass, setPlayerClass] = useState(null);
    const [boss, setBoss] = useState('');
    const [a2aEndpoint, setA2aEndpoint] = useState('http://localhost:8080/player-agent');
    const { setBackground } = useBackground();

    const playerClasses = ['Summoner', 'Shadowblade', 'Guardian', 'Scholar'];
    const bossOptions = ["Procrastination", "Hype", "Dogma", "Legacy", "Perfectionism", "Obfuscation", "Apathy"];

    useEffect(() => {
        setBackground('/assets/images/enterinfo.png');
        const randomBoss = bossOptions[Math.floor(Math.random() * bossOptions.length)];
        setBoss(randomBoss);
    }, [setBackground]);

    useEffect(() => {
        try {
            const url = new URL(a2aEndpoint);
            const host = url.hostname; // Use hostname from the input URL
            const foundClass = playerClasses.find(c => host.toLowerCase().startsWith(c.toLowerCase() + '-agent'));
            setPlayerClass(foundClass || null);
        } catch (error) {
            // Invalid URL, so no class can be determined
            setPlayerClass(null);
        }
    }, [a2aEndpoint]); // Re-run when a2aEndpoint changes

    const handleStart = () => {
        if (playerClass) {
            onGameStart('mini', { player_class: playerClass, boss_name: boss, a2a_endpoint: a2aEndpoint });
        }
    };

    return (
        <div className="main-menu">
            <h1>Mini Boss Dungeon</h1>
            <div className="menu-section">
                <div className="form-group">
                    <label>A2A Endpoint:</label>
                    <input type="text" value={a2aEndpoint} onChange={(e) => setA2aEndpoint(e.target.value)} placeholder="e.g., http://guardian-agent.localhost:8080" />
                </div>
                <div className="form-group">
                    <label>Your Class:</label>
                    <input type="text" value={playerClass || 'Unknown'} readOnly style={{ cursor: 'not-allowed', backgroundColor: '#444' }} />
                </div>
                <div className="form-group">
                    <label>Your Opponent:</label>
                    <input type="text" value={boss} readOnly style={{ cursor: 'not-allowed', backgroundColor: '#444' }} />
                </div>
                <button className="btn" onClick={handleStart} disabled={!playerClass}>Enter</button>
                {!playerClass && <p className="error-message">Could not determine player class from A2A endpoint hostname. The hostname should start with a valid class name (e.g., 'guardian-agent...').</p>}
            </div>
        </div>
    );
};

export default MiniBossPage;