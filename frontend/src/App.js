import React, { useState } from 'react';
import { useBackground } from './contexts/BackgroundContext';
import axios from 'axios';
import { Routes, Route, useNavigate, useLocation } from 'react-router-dom';

import CombatScreen from './components/CombatScreen';
import PreCombatScreen from './components/PreCombatScreen';
import MiniBossPage from './pages/MiniBossPage';
import UltimateBossPage from './pages/UltimateBossPage';
import HomePage from './pages/HomePage';
import './styles.css';

const API_URL = '';

function App() {
    const [preGameState, setPreGameState] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const { setBackground } = useBackground();

    const location = useLocation();
    const showReturnHomeButton = location.pathname === '/combat' || location.pathname === '/pre-combat';

    const handleGameStart = async (gameType, params) => {
        try {
            const endpoint = gameType === 'mini' ? '/api/miniboss/start' : '/api/ultimateboss/start';
            const url = `${API_URL}${endpoint}`;
            console.log(`Making API call to: ${url}`);
            const response = await axios.post(url, params);
            setPreGameState(response.data);
            setError(null);
            navigate('/pre-combat');
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to start game.');
        }
    };

    const handleAction = async (gameId, action) => {
        try {
            const url = `${API_URL}/api/game/${gameId}/action`;
            console.log(`Making API call to: ${url}`);
            const response = await axios.post(url, action);
            setGameState(response.data);
            return response.data;
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to perform action.');
        }
    };

    const handleFightStart = () => {
        if (preGameState) {
            if (preGameState.game_type === 'mini') {
                const backgrounds = ['/assets/images/bf-bg-1.png', '/assets/images/bf-bg-2.png', '/assets/images/bf-bg-3.png', '/assets/images/bf-bg-4.png'];
                const randomBg = backgrounds[Math.floor(Math.random() * backgrounds.length)];
                setBackground(randomBg);
            } else if (preGameState.game_type === 'ultimate') {
                setBackground('/assets/images/bf-ultimate.png');
            }
        }
        setGameState(preGameState);
        setPreGameState(null);
        navigate('/combat');
    };

    const resetToMenu = () => {
        setGameState(null);
        setError(null);
        navigate('/');
    };

    const pollGameState = async (gameId) => {
        try {
            const url = `${API_URL}/api/game/${gameId}`;
            console.log(`Making API call to: ${url}`);
            const response = await axios.get(url);
            setGameState(response.data);
            return response.data;
        } catch (err) {
            console.error("Polling error:", err);
        }
    };

    return (
        <div className="App">
            {error && <div className="error-message">{error}</div>}
            <Routes>
                <Route path="/" element={<HomePage />} />
                <Route path="/mini-boss" element={<MiniBossPage onGameStart={handleGameStart} />} />
                <Route path="/ultimate-boss" element={<UltimateBossPage onGameStart={handleGameStart} />} />
                <Route path="/pre-combat" element={preGameState ? <PreCombatScreen gameState={preGameState} onStartFight={handleFightStart} /> : null} />
                <Route path="/combat" element={<CombatScreen gameState={gameState} onAction={handleAction} onReset={resetToMenu} pollGameState={pollGameState} />} />
            </Routes>
            {showReturnHomeButton && (
                <button onClick={resetToMenu} className="btn return-home-btn">Return to Home</button>
            )}
        </div>
    );
}

export default App;
