import React, { useEffect, useState } from 'react';
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

// Helper function to create a delay
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const CombatScreen = ({ gameState, onAction, onReset, pollGameState }) => {
    const [showQuiz, setShowQuiz] = useState(false);
    const [bossDialog, setBossDialog] = useState(null);
    const [playerDialog, setPlayerDialog] = useState(null);
    const [statusMessage, setStatusMessage] = useState("");
    const [actingCharacter, setActingCharacter] = useState(null);

    const { setBackground } = useBackground();

    useEffect(() => {
        if (!gameState) return;

        // Set the background
        if (gameState.game_type === 'mini') {
            setBackground(randomBg);
        } else if (gameState.game_type === 'ultimate') {
            setBackground('/assets/images/bf-ultimate.png');
        }

        // Set the status message
        setStatusMessage(gameState.status_message);

        // Set the active character and handle the turn
        console.log('Setting acting character:', gameState.current_turn);
        setActingCharacter(gameState.current_turn);

        if (gameState.current_turn === 'boss') {
            handleBossTurn(gameState);
        } else {
            setShowQuiz(true);
        }
    }, [gameState, setBackground]);

    const handleBossTurn = async (currentGame) => {
        setStatusMessage(`Waiting for ${currentGame.boss.name}...`);
        await wait(4000);

        const newGameState = await pollGameState(currentGame.game_id);
        if (!newGameState) return;

        setBossDialog(newGameState.last_boss_attack);
        await wait(5000);
        setBossDialog(null);

        if (newGameState.game_over) return;

        setShowQuiz(true);
    };

    const handleAnswer = async (answerIndex) => {
        if (!gameState || gameState.game_over) return;

        const currentQuiz = gameState.active_quiz;

        setShowQuiz(false);
        const newGameState = await onAction(gameState.game_id, { answer_index: answerIndex });
        if (!newGameState) return;

        if (currentQuiz) {
            setPlayerDialog({ id: newGameState.current_turn, msg: currentQuiz.msg });
        }

        await wait(3000);
        setPlayerDialog(null);
    };

    if (!gameState) {
        return null;
    }

    if (gameState.game_over) {
        return <GameOverScreen gameState={gameState} onReset={onReset} />;
    }

    return (
        <div className="combat-screen">
            <StatusDisplay message={statusMessage} />
            <div className="characters-wrapper">
                <div className="character-container">
                    <Boss
                        boss={gameState.boss}
                        isTurn={actingCharacter === 'boss'}
                        dialog={bossDialog}
                    />
                </div>

                <div className={`character-container ${gameState.players.length > 1 ? 'party-container' : ''}`}>
                    {gameState.players.map(player => (
                        <Player
                            key={player.id}
                            player={player}
                            isTurn={actingCharacter === player.id}
                            dialog={playerDialog && playerDialog.id === player.id ? playerDialog.msg : null}
                        />
                    ))}
                </div>
            </div>
            <QuizModal quiz={showQuiz ? gameState.active_quiz : null} onAnswer={handleAnswer} />
        </div>
    );
};

export default CombatScreen;
