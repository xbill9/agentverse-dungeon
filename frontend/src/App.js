import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MainMenu from './components/MainMenu';
import CombatScreen from './components/CombatScreen';
import PreCombatScreen from './components/PreCombatScreen';
import MiniBossPage from './pages/MiniBossPage';
import UltimateBossPage from './pages/UltimateBossPage';
import './styles.css';

const API_URL = 'http://localhost:8000';

function App() {
    const [preGameState, setPreGameState] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [error, setError] = useState(null);
    const [page, setPage] = useState('menu');

    const handleGameStart = async (gameType, params) => {
        try {
            const endpoint = gameType === 'mini' ? '/api/miniboss/start' : '/api/ultimateboss/start';
            const response = await axios.post(`${API_URL}${endpoint}`, params);
            setPreGameState(response.data);
            setError(null);
            setPage('pre-combat');
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to start game.');
        }
    };

    const handleAction = async (gameId, answerIndex) => {
        try {
            const response = await axios.post(`${API_URL}/api/game/${gameId}/action`, { answer_index: answerIndex });
            setGameState(response.data);
        } catch (err) {
            setError(err.response?.data?.detail ? JSON.stringify(err.response.data.detail) : 'Failed to perform action.');
        }
    };

    const handleFightStart = () => {
        setGameState(preGameState);
        setPreGameState(null);
        setPage('combat');
    };

    const resetToMenu = () => {
        setGameState(null);
        setError(null);
        setPage('menu');
    };

    const pollGameState = async (gameId) => {
        try {
            const response = await axios.get(`${API_URL}/api/game/${gameId}`);
            setGameState(response.data);
        } catch (err) {
            console.error("Polling error:", err);
        }
    };

    const renderPage = () => {
        switch (page) {
            case 'mini-boss':
                return <MiniBossPage onGameStart={handleGameStart} />;
            case 'ultimate-boss':
                return <UltimateBossPage onGameStart={handleGameStart} />;
            case 'pre-combat':
                return <PreCombatScreen gameState={preGameState} onStartFight={handleFightStart} />;
            case 'combat':
                return <CombatScreen gameState={gameState} onAction={handleAction} onReset={resetToMenu} pollGameState={pollGameState} />;
            default:
                return <MainMenu setPage={setPage} />;
        }
    };

    return (
        <div className="App">
            {error && <div className="error-message">{error}</div>}
            {renderPage()}
        </div>
    );
}

export default App;
