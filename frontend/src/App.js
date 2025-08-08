import React, { useState, useEffect } from 'react';
import { useBackground } from './contexts/BackgroundContext';
import axios from 'axios';
import { Routes, Route, useNavigate } from 'react-router-dom';
import MainMenu from './components/MainMenu';
import CombatScreen from './components/CombatScreen';
import PreCombatScreen from './components/PreCombatScreen';
import MiniBossPage from './pages/MiniBossPage';
import UltimateBossPage from './pages/UltimateBossPage';
import HomePage from './pages/HomePage';
import './styles.css';

const API_URL = 'http://localhost:8000';

function App() {
    const [preGameState, setPreGameState] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const { setBackground } = useBackground();

    const handleGameStart = async (gameType, params) => {
        try {
            const endpoint = gameType === 'mini' ? '/api/miniboss/start' : '/api/ultimateboss/start';
            const response = await axios.post(`${API_URL}${endpoint}`, params);
            setPreGameState(response.data);
            setError(null);
            navigate('/pre-combat');
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to start game.');
        }
    };

    const handleAction = async (gameId, action) => {
        try {
            const response = await axios.post(`${API_URL}/api/game/${gameId}/action`, action);
            setGameState(response.data);
            return response.data;
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to perform action.');
        }
    };

    const handleFightStart = () => {
        if (preGameState) {
            if (preGameState.game_type === 'mini-boss') {
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
            const response = await axios.get(`${API_URL}/api/game/${gameId}`);
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
                <Route path="/pre-combat" element={preGameState ? <PreCombatScreen gameState={preGameState} onStartFight={handleFightStart} /> : <HomePage />} />
                <Route path="/combat" element={<CombatScreen gameState={gameState} onAction={handleAction} onReset={resetToMenu} pollGameState={pollGameState} />} />
            </Routes>
        </div>
    );
}

export default App;
