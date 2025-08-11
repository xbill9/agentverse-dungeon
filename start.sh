#!/bin/bash

# Start the backend in the background
echo "Starting backend..."
cd /app/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start the frontend in the foreground
echo "Starting frontend..."
cd /app/frontend
npm start