import React, { useEffect } from 'react';
import { useBackground } from '../contexts/BackgroundContext';
import Boss from './Boss';
import Player from './Player';

const PreCombatScreen = ({ gameState, onStartFight }) => {
    const { setBackground } = useBackground();

    useEffect(() => {
        setBackground('/assets/images/enterinfo.png');
    }, []);
    return (
        <div className="pre-combat-screen">
            <h1>Get Ready to Fight!</h1>
            <div className="pre-combat-characters">
                <div className="character-container">
                    <Boss boss={gameState.boss} />
                </div>
                <div className={`character-container ${gameState.players.length > 1 ? 'party-container' : ''}`}>
                    {gameState.players.map(player => (
                        <Player key={player.id} player={player} />
                    ))}
                </div>
            </div>
            <button onClick={onStartFight} className="btn btn-ultimate">Start Fight</button>
        </div>
    );
};

export default PreCombatScreen;
