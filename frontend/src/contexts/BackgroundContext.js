import React, { createContext, useState, useContext, useEffect, useMemo } from 'react';

const BackgroundContext = createContext();

export const useBackground = () => useContext(BackgroundContext);

export const BackgroundProvider = ({ children }) => {
  const [background, setBackground] = useState('');

  useEffect(() => {
    console.log('Background changed to:', background);
    if (background) {
      document.body.style.backgroundImage = `url(${background})`;
      document.body.style.backgroundSize = 'cover';
      document.body.style.backgroundRepeat = 'no-repeat';
      document.body.style.backgroundPosition = 'center center';
    } else {
      document.body.style.backgroundImage = 'none';
      document.body.style.backgroundColor = '#1a1a1a'; // Default background color
    }
  }, [background]);

  const value = useMemo(() => ({ setBackground }), []);

  return (
    <BackgroundContext.Provider value={value}>
      {children}
    </BackgroundContext.Provider>
  );
};
