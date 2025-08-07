import React from 'react';

const StatusDisplay = ({ message }) => {
    if (!message) return null;

    return (
        <div className="status-display">
            {message}
        </div>
    );
};

export default StatusDisplay;
