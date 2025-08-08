
import React, { useEffect, useState } from 'react';

const DamageIndicator = ({ damage, characterName }) => {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        if (damage) {
            console.log(`DamageIndicator: Rendering with damage: ${damage} for ${characterName}`);
            setVisible(true);
            const timer = setTimeout(() => {
                setVisible(false);
            }, 5000);
            return () => clearTimeout(timer);
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
