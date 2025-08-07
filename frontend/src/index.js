import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './styles.css';
import { BackgroundProvider } from './contexts/BackgroundContext';
import { BrowserRouter } from 'react-router-dom';

const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <BackgroundProvider>
        <App />
      </BackgroundProvider>
    </BrowserRouter>
  </React.StrictMode>
);
