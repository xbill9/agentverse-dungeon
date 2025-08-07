import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MainMenu from './components/MainMenu';
import CombatScreen from './components/CombatScreen';
import PreCombatScreen from './components/PreCombatScreen';
import './styles.css';

const API_URL = 'http://localhost:8000';

function App() {
    const [preGameState, setPreGameState] = useState(null);
    const [gameState, setGameState] = useState(null);
    const [error, setError] = useState(null);

    const handleGameStart = async (gameType, params) => {
        try {
            const endpoint = gameType === 'mini' ? '/api/miniboss/start' : '/api/ultimateboss/start';
            const response = await axios.post(`${API_URL}${endpoint}`, params);
            setPreGameState(response.data);
            setError(null);
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to start game.');
        }
    };

    const handleAction = async (gameId, answerIndex) => {
        try {
            const response = await axios.post(`${API_URL}/api/game/${gameId}/action`, { answer_index: answerIndex });
            setGameState(response.data);
        } catch (err) {
            setError(err.response?.data?.detail || 'Failed to perform action.');
        }
    };

    const handleFightStart = () => {
        setGameState(preGameState);
        setPreGameState(null);
    };

    const resetToMenu = () => {
        setGameState(null);
        setError(null);
    };

    const pollGameState = async (gameId) => {
        try {
            const response = await axios.get(`${API_URL}/api/game/${gameId}`);
            setGameState(response.data);
        } catch (err) {
            console.error("Polling error:", err);
        }
    };


    return (
        <div className="App">
            {error && <div className="error-message">{error}</div>}
            {preGameState ? (
                <PreCombatScreen gameState={preGameState} onStartFight={handleFightStart} />
            ) : !gameState ? (
                <MainMenu onGameStart={handleGameStart} />
            ) : (
                <CombatScreen 
                    gameState={gameState} 
                    onAction={handleAction} 
                    onReset={resetToMenu}
                    pollGameState={pollGameState}
                />
            )}
        </div>
    );
}

export default App;