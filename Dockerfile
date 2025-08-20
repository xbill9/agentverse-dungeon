# Stage 1: Build the frontend
FROM node:20-alpine AS builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Create the final image
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/frontend/build ./frontend/build
COPY backend/ ./backend/
COPY start.sh ./
RUN pip install --no-cache-dir -r backend/requirements.txt
EXPOSE 8000
CMD ["./start.sh"]
