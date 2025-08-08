import React from 'react';

const HpBar = ({ current, max }) => {
    const percentage = (current / max) * 100;
    let barClass = 'hp-bar';
    if (percentage < 50) barClass += ' low';
    if (percentage < 25) barClass += ' critical';

    // By adding a key that changes with the `current` value, we force React
    // to re-render the component from scratch whenever the HP changes,
    // ensuring the animation is not skipped.
    return (
        <div className="hp-bar-container" title={`${current} / ${max} HP`} key={current}>
            <div className={barClass} style={{ width: `${percentage}%` }}>
                {current}
            </div>
        </div>
    );
};

export default HpBar;
