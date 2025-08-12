import React from 'react';
import HpBar from './HpBar';
import DialogBubble from './DialogBubble';
import DamageIndicator from './DamageIndicator';
import AttackEffect from './AttackEffect';

const Boss = ({ boss, isTurn, dialog, effectClass, cyclingDialog, gameType }) => {
    const imageName = isTurn ? `${boss.name}-motion` : boss.name;
    const imageSrc = `/assets/images/bosses/${imageName}.png`;
    console.log('Boss component - gameType:', gameType);
    return (
        <div className={`character boss ${isTurn ? 'turn-active' : ''} ${effectClass} ${gameType !== 'ultimate' ? 'mini-boss-size' : ''}`}>
            <AttackEffect trigger={boss.last_damage_taken} />
            <DamageIndicator damage={boss.last_damage_taken} characterName={boss.name} />
            <DialogBubble message={dialog} /> {/* For attack message */}
            {isTurn && cyclingDialog && <DialogBubble message={cyclingDialog} duration={6000} className="rotating" />} {/* For cycling dialog */}
            <div className="character-image-wrapper">
                <img src={imageSrc} alt={boss.name} className="character-image" />
            </div>
            <div className="character-info">
                <div className="character-name">{boss.name}</div>
                <HpBar current={boss.hp} max={boss.max_hp} />
            </div>
        </div>
    );
};

export default Boss;