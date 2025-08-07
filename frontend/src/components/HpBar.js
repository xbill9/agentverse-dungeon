import React from 'react';

const HpBar = ({ current, max }) => {
    const percentage = (current / max) * 100;
    let barClass = 'hp-bar';
    if (percentage < 50) barClass += ' low';
    if (percentage < 25) barClass += ' critical';

    return (
        <div className="hp-bar-container" title={`${current} / ${max} HP`}>
            <div className={barClass} style={{ width: `${percentage}%` }}>
                {current}
            </div>
        </div>
    );
};

export default HpBar;
