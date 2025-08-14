import React, { useEffect, useState } from 'react';

const imageList = [
    '/assets/images/attack/attack-1.png',
    '/assets/images/attack/attack-2.png',
    '/assets/images/attack/attack-3.png',
    '/assets/images/attack/attack-4.png',
    '/assets/images/attack/attack-5.png'
];

const AttackEffect = ({ trigger, damageEventId }) => {
    const [visible, setVisible] = useState(false);
    const [imageSrc, setImageSrc] = useState('');

    useEffect(() => {
        let timer;

        if (trigger > 0) {
            const randomImage = imageList[Math.floor(Math.random() * imageList.length)];
            setImageSrc(randomImage);
            setVisible(true);
            timer = setTimeout(() => {
                setVisible(false);
            }, 4000);
        } else {
            setVisible(false); // Hide if trigger is 0 or null
        }

        return () => {
            clearTimeout(timer);
            setVisible(false); // Ensure it's hidden on cleanup
        };
    }, [trigger, damageEventId]);

    if (!visible) {
        return null;
    }

    return <div className="attack-effect" style={{ backgroundImage: `url(${imageSrc})` }}></div>;
};

export default AttackEffect;