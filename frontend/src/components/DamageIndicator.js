
import React, { useEffect, useState } from 'react';

const DamageIndicator = ({ damage, characterName }) => {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        if (damage) {
            const showTimer = setTimeout(() => {
                setVisible(true);
            }, 300); // Delay to show after attack effect

            const timer = setTimeout(() => {
                setVisible(false);
            }, 16000);
            return () => {
                clearTimeout(showTimer);
                clearTimeout(timer);
            };
        }
    }, [damage, characterName]);

    if (!visible) {
        return null;
    }

    return (
        <div className="damage-indicator">
            -{damage}
        </div>
    );
};

export default DamageIndicator;
