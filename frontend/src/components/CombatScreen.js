import React, { useEffect, useState } from 'react';
import Boss from './Boss';
import Player from './Player';
import QuizModal from './QuizModal';
import StatusDisplay from './StatusDisplay';

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

// Helper function to create a delay
const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const animationEffects = ['effect-shake', 'effect-pulsate-glow', 'effect-desaturate', 'effect-flip-and-shake'];

const CombatScreen = ({ gameState, onAction, onReset, pollGameState }) => {
    const [showQuiz, setShowQuiz] = useState(false);
    const [bossDialog, setBossDialog] = useState(null); // For boss attack message
    const [bossCyclingDialog, setBossCyclingDialog] = useState(null); // For cycling boss dialog
    const [playerDialog, setPlayerDialog] = useState(null);
    const [statusMessage, setStatusMessage] = useState("");
    const [actingCharacter, setActingCharacter] = useState(null);
    const [currentEffect, setCurrentEffect] = useState('');

    useEffect(() => {
        let intervalId;

        if (actingCharacter) {
            let effectIndex = 0;
            const cycleEffects = () => {
                setCurrentEffect(animationEffects[effectIndex]);
                effectIndex = (effectIndex + 1) % animationEffects.length;
            };
            cycleEffects();
            intervalId = setInterval(cycleEffects, 6000);
        }

        return () => {
            if (intervalId) {
                clearInterval(intervalId);
            }
            setCurrentEffect('');
        };
    }, [actingCharacter]);

    useEffect(() => {
        let dialogIntervalId;
        if (actingCharacter === 'boss' && gameState && gameState.boss.dialog_phrases.length > 0) {
            let dialogIndex = Math.floor(Math.random() * gameState.boss.dialog_phrases.length); // Start from a random phrase
            const cycleBossDialog = () => {
                setBossCyclingDialog(gameState.boss.dialog_phrases[dialogIndex]);
                dialogIndex = (dialogIndex + 1) % gameState.boss.dialog_phrases.length;
            };
            cycleBossDialog(); // Display first dialog immediately
            dialogIntervalId = setInterval(cycleBossDialog, 6000); // Cycle every 6 seconds
        } else {
            setBossCyclingDialog(null); // Clear dialog when not boss's turn
        }

        return () => {
            if (dialogIntervalId) {
                clearInterval(dialogIntervalId);
            }
        };
    }, [actingCharacter, gameState]); // Depend on actingCharacter and gameState for phrases

    useEffect(() => {
        if (!gameState) return;

        setStatusMessage(gameState.status_message);
        setActingCharacter(gameState.current_turn);

        if (gameState.current_turn === 'boss') {
            handleBossTurn(gameState);
        } else {
            setShowQuiz(true);
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [gameState]);

    const handleBossTurn = async (currentGame) => {
        setStatusMessage(`Waiting for ${currentGame.boss.name}...`);
        await wait(4000);

        const newGameState = await pollGameState(currentGame.game_id);
        if (!newGameState) return;

        setBossDialog(newGameState.last_boss_attack);
        await wait(8000);
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
            setPlayerDialog({ id: gameState.current_turn, msg: currentQuiz.msg });
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
                        effectClass={actingCharacter === 'boss' ? currentEffect : ''}
                        cyclingDialog={bossCyclingDialog}
                        gameType={gameState.game_type}
                    />
                </div>

                <div className={`character-container ${gameState.players.length > 1 ? 'party-container' : ''}`}>
                    {gameState.players.map(player => (
                        <Player
                            key={player.id}
                            player={player}
                            isTurn={actingCharacter === player.id}
                            dialog={playerDialog && playerDialog.id === player.id ? playerDialog.msg : null}
                            effectClass={actingCharacter === player.id ? currentEffect : ''}
                        />
                    ))}
                </div>
            </div>
            <QuizModal quiz={showQuiz ? gameState.active_quiz : null} onAnswer={handleAnswer} />
        </div>
    );
};

export default CombatScreen;
