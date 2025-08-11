FROM node:18-alpine

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r ./backend/requirements.txt

# Install frontend dependencies
COPY frontend/package.json frontend/package-lock.json ./frontend/
RUN cd frontend && npm install

# Copy the rest of the app code
COPY . .

# Expose ports
EXPOSE 3000 8000

# Make start script executable and set it as the command
COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]