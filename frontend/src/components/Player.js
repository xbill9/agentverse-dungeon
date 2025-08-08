import React, { useEffect } from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';

const Player = ({ player, isTurn, dialog }) => {
    const imageName = isTurn ? `${player.player_class}-motion` : player.player_class;
    const imageSrc = `/assets/images/players/${imageName}.png`;
    return (
        <div className={`character ${isTurn ? 'turn-active' : ''}`}>
            <DamageIndicator damage={player.last_damage_taken} characterName={player.player_class} />
            <DialogBubble message={dialog} duration={5000} />
            <img src={imageSrc} alt={player.player_class} className="character-image" />
            <div className="character-info">
                <div className="character-name">{player.player_class}</div>
                <HpBar current={player.hp} max={player.max_hp} />
            </div>
        </div>
    );
};

export default Player;
