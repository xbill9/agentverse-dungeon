import React, { createContext, useState, useContext, useEffect } from 'react';

const BackgroundContext = createContext();

export const useBackground = () => useContext(BackgroundContext);

export const BackgroundProvider = ({ children }) => {
  const [background, setBackground] = useState('');

  useEffect(() => {
    
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

  return (
    <BackgroundContext.Provider value={{ setBackground }}>
      {children}
    </BackgroundContext.Provider>
  );
};
