
import React, { useEffect, useState } from 'react';

const DamageIndicator = ({ damage }) => {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        if (damage) {
            console.log('DamageIndicator: Rendering with damage:', damage);
            setVisible(true);
            const timer = setTimeout(() => {
                setVisible(false);
            }, 3000);
            return () => clearTimeout(timer);
        }
    }, [damage]);

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
