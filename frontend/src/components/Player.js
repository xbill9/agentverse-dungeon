import React from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';

const Player = ({ player, isTurn, dialog, imageSrc }) => {
    return (
        <div className={`character ${isTurn ? 'turn-active' : ''}`}>
            <DamageIndicator damage={player.last_damage_taken} />
            <DialogBubble message={dialog} />
            <img src={imageSrc} alt={player.player_class} className="character-image" />
            <div className="character-name">{player.player_class}</div>
            <HpBar current={player.hp} max={player.max_hp} />
        </div>
    );
};

export default Player;
