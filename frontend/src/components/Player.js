import React from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';
import AttackEffect from './AttackEffect';

const Player = ({ player, isTurn, dialog, effectClass }) => {
    const imageName = isTurn ? `${player.player_class}-motion` : player.player_class;
    const imageSrc = `/assets/images/players/${imageName}.png`;
    return (
        <div className={`character ${player.player_class} ${isTurn ? 'turn-active' : ''} ${effectClass}`}>
            <AttackEffect trigger={player.last_damage_taken} />
            <DamageIndicator damage={player.last_damage_taken} characterName={player.player_class} />
            <DialogBubble message={dialog} />
            <div className="character-image-wrapper">
                <img src={imageSrc} alt={player.player_class} className="character-image" />
            </div>
            <div className="character-info">
                <div className="character-name">{player.player_class}</div>
                <HpBar current={player.hp} max={player.max_hp} />
            </div>
        </div>
    );
};

export default Player;
