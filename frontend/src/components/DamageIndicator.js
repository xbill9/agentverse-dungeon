
import React, { useEffect, useState } from 'react';

const DamageIndicator = ({ damage, characterName, damageEventId }) => {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        let showTimer;
        let hideTimer;

        if (damage > 0) {
            showTimer = setTimeout(() => {
                setVisible(true);
            }, 300); // Delay to show after attack effect

            hideTimer = setTimeout(() => {
                setVisible(false);
            }, 16000); // Duration of the indicator
        } else {
            setVisible(false); // Hide if damage is 0 or null
        }

        return () => {
            clearTimeout(showTimer);
            clearTimeout(hideTimer);
            setVisible(false); // Ensure it's hidden on cleanup
        };
    }, [damage, damageEventId]);

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
