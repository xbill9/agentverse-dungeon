import React, { useEffect, useState, useRef } from 'react';
import Boss from './Boss';
import Player from './Player';
import QuizModal from './QuizModal';
import StatusDisplay from './StatusDisplay';
import { useBackground } from '../contexts/BackgroundContext';

const GameOverScreen = ({ gameState, onReset }) => {
    const { player_won, game_type, boss } = gameState;

    let message;
    if (player_won) {
        if (game_type === 'ultimate') {
            message = `Congratulations! You have conquered ${boss.name}!`;
        } else {
            message = `You are victorious against ${boss.name}!`;
        }
    } else {
        message = `You have been defeated by ${boss.name}.`;
    }

    return (
        <div className="game-over-screen">
            <h1 className={player_won ? 'win' : 'loss'}>{message}</h1>
            <button onClick={onReset} className="btn">Return to Main Menu</button>
        </div>
    );
};
const backgrounds = ['/assets/images/bf-bg-1.png', '/assets/images/bf-bg-2.png', '/assets/images/bf-bg-3.png', '/assets/images/bf-bg-4.png'];
const ranNum = Math.random() * backgrounds.length
const randomBg = backgrounds[Math.floor(ranNum)];

const CombatScreen = ({ gameState, onAction, onReset, pollGameState }) => {
    const [displayGameState, setDisplayGameState] = useState(gameState);
    const [showQuiz, setShowQuiz] = useState(false);
    const [bossDialog, setBossDialog] = useState(null);
    const [playerDialog, setPlayerDialog] = useState(null);
    const [statusMessage, setStatusMessage] = useState("");

    const { setBackground } = useBackground();
    const prevGameStateRef = useRef();
    

        useEffect(() => {
        

        prevGameStateRef.current = gameState;
        const prevGameState = prevGameStateRef.current;

        if (!gameState) {
            return; // Exit early if gameState is null or undefined
        }
        
        // --- Background Logic ---
        if (!gameState.game_over) {
            if (gameState.game_type === 'mini') {
                setBackground(randomBg);
            } else if (gameState.game_type === 'ultimate') {
                setBackground('/assets/images/bf-ultimate.png');
            }
        }

        setDisplayGameState(gameState);
        setStatusMessage(gameState.status_message);
        
        
        if (gameState.boss) {
            console.log('CombatScreen: Boss HP', gameState.boss.current_hp);
        }

        if (gameState.game_over) {
            setShowQuiz(false);
            return;
        }

        // --- Animation & Dialog Logic ---
        if (gameState.active_quiz) {
            // Add a delay for the second attack
            if (prevGameState && prevGameState.active_quiz && prevGameState.current_turn === gameState.current_turn) {
                setTimeout(() => setShowQuiz(true), 1500);
            } else {
                setShowQuiz(true);
            }
            const activePlayer = gameState.players.find(p => p.id === gameState.current_turn);
            if (activePlayer) {
                setPlayerDialog({ id: activePlayer.id, msg: gameState.active_quiz.msg });
            }
        } else {
            setShowQuiz(false);
        }

        if (gameState.last_boss_attack) {
            console.log('CombatScreen: Setting bossDialog to', gameState.last_boss_attack);
            setBossDialog(gameState.last_boss_attack);
        } else {
            console.log('CombatScreen: gameState.last_boss_attack is null or empty');
        }

        // --- Turn Advancement Logic ---
        if (gameState.current_turn === 'boss' && !gameState.game_over) {
            const bossTurnPolling = setInterval(() => {
                pollGameState(gameState.game_id);
            }, 2000); // Poll every 2 seconds during boss turn
            return () => clearInterval(bossTurnPolling);
        }
        

    }, [gameState, pollGameState, setBackground, showQuiz]);

    const handleAnswer = (answerIndex) => {
        if (displayGameState.game_over) {
            return <GameOverScreen gameState={displayGameState} onReset={onReset} />;
        }
        console.log('Quiz answer clicked:', answerIndex);
        setShowQuiz(false);
        setPlayerDialog(null);
        onAction(gameState.game_id, answerIndex);
        pollGameState(gameState.game_id); // Poll for updated game state immediately after player action
    };

    if (!displayGameState) {
        return null; // Or a loading spinner
    }

    if (displayGameState.game_over) {
        return <GameOverScreen gameState={displayGameState} onReset={onReset} />;
    }

    return (
        <div className="combat-screen">
            <StatusDisplay message={statusMessage} />
            <div className="characters-wrapper">
                <div className="character-container">
                    <Boss 
                        boss={displayGameState.boss} 
                        isTurn={displayGameState.current_turn === 'boss'}
                        dialog={bossDialog}
                    />
                </div>

                <div className={`character-container ${displayGameState.players.length > 1 ? 'party-container' : ''}`}>
                    {displayGameState.players.map(player => (
                        <Player 
                            key={player.id} 
                            player={player}
                            isTurn={player.id === displayGameState.current_turn}
                            dialog={playerDialog && playerDialog.id === player.id ? playerDialog.msg : null}
                        />
                    ))}
                </div>
            </div>
            <QuizModal quiz={showQuiz ? displayGameState.active_quiz : null} onAnswer={handleAnswer} />
        </div>
    );
};

export default CombatScreen;
