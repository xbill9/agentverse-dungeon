import React, { useState, useEffect } from 'react';

const DialogBubble = ({ message, duration = 10000 }) => {
    const [visible, setVisible] = useState(false);

    useEffect(() => {
        if (message) {
            setVisible(true);
            const timer = setTimeout(() => {
                setVisible(false);
            }, duration);
            return () => clearTimeout(timer);
        } else {
            setVisible(false);
        }
    }, [message, duration]);

    return (
        <div className={`dialog-bubble ${visible ? 'visible' : ''}`}>
            {message}
        </div>
    );
};

export default DialogBubble;
