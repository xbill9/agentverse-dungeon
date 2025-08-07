import React from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';

const Boss = ({ boss, isTurn, dialog }) => {
    return (
        <div className={`character boss ${isTurn ? 'turn-active' : ''}`}>
            <DamageIndicator damage={boss.last_damage_taken} />
            <DialogBubble message={dialog} />
            <div className="character-name">{boss.name}</div>
            <HpBar current={boss.hp} max={boss.max_hp} />
        </div>
    );
};

export default Boss;