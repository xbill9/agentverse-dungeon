FROM node:18-alpine

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

WORKDIR /app

# Install backend dependencies
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r ./backend/requirements.txt --break-system-packages

# Install frontend dependencies
COPY frontend/package.json frontend/package-lock.json ./frontend/
RUN cd frontend && npm install

# Copy the rest of the app code
COPY . .

# === DEBUGGING AND FIXING THE SCRIPT ===
# Step 1: Prove the script exists and check its initial permissions.
RUN echo "--- Verifying start.sh exists after copy ---" && \
    ls -la /app

# Step 2: Ensure the script has the correct shebang, fix line endings, and make it executable.
# This adds #!/bin/sh if it's missing from the first line.
RUN sed -i '1s,^#!/bin/sh,,' /app/start.sh && \
    sed -i '1i#!/bin/sh' /app/start.sh && \
    sed -i 's/\r$//' /app/start.sh && \
    chmod +x /app/start.sh

# Step 3: Display the script's contents to confirm the shebang and permissions.
RUN echo "--- Verifying script content and permissions after fix ---" && \
    ls -la /app/start.sh && \
    echo "--- Script Content ---" && \
    cat /app/start.sh && \
    echo "--- End of Script ---"

# Expose ports
EXPOSE 3000 8000

# Set the command to run the script using its absolute path.
CMD ["/app/start.sh"]