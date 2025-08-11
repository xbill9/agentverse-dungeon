import React from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';

const Boss = ({ boss, isTurn, dialog, effectClass }) => {
    const imageName = isTurn ? `${boss.name}-motion` : boss.name;
    const imageSrc = `/assets/images/bosses/${imageName}.png`;
    return (
        <div className={`character boss ${isTurn ? 'turn-active' : ''} ${effectClass}`}>
            <DamageIndicator damage={boss.last_damage_taken} characterName={boss.name} />
            <DialogBubble message={dialog} />
            <img src={imageSrc} alt={boss.name} className="character-image" />
            <div className="character-info">
                <div className="character-name">{boss.name}</div>
                <HpBar current={boss.hp} max={boss.max_hp} />
            </div>
        </div>
    );
};

export default Boss;