import React, { useEffect, useState } from 'react';

const imageList = [
    '/assets/images/attack/attack-1.png',
    '/assets/images/attack/attack-2.png',
    '/assets/images/attack/attack-3.png',
    '/assets/images/attack/attack-4.png',
    '/assets/images/attack/attack-5.png'
];

const AttackEffect = ({ trigger }) => {
    const [visible, setVisible] = useState(false);
    const [imageSrc, setImageSrc] = useState('');

    useEffect(() => {
        if (trigger) {
            const randomImage = imageList[Math.floor(Math.random() * imageList.length)];
            setImageSrc(randomImage);
            setVisible(true);
            const timer = setTimeout(() => {
                setVisible(false);
            }, 4000);
            return () => clearTimeout(timer);
        }
    }, [trigger]);

    if (!visible) {
        return null;
    }

    return <div className="attack-effect" style={{ backgroundImage: `url(${imageSrc})` }}></div>;
};

export default AttackEffect;