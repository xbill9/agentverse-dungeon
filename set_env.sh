#!/bin/bash

# This script sets various Google Cloud related environment variables.
# It must be SOURCED to make the variables available in your current shell.

# Example: source ./set_env.sh

# --- Configuration ---
PROJECT_FILE="~/project_id.txt"
# This base name is for other workshops; Summoner's variables are defined below.
export REPO_NAME="agentverse-repo"
# ---------------------


echo "--- Setting Google Cloud Environment Variables ---"

# --- Authentication Check ---
echo "Checking gcloud authentication status..."

# Run a command that requires authentication (like listing accounts or printing a token)
# Redirect stdout and stderr to /dev/null so we don't see output unless there's a real error

if gcloud auth print-access-token > /dev/null 2>&1; then
  echo "gcloud is authenticated."
else
  echo "Error: gcloud is not authenticated."
  echo "Please log in by running: gcloud auth login"
  return 1
fi
# --- --- --- --- --- ---



# 1. Check if project file exists
PROJECT_FILE_PATH=$(eval echo $PROJECT_FILE) # Expand potential ~
if [ ! -f "$PROJECT_FILE_PATH" ]; then
  echo "Error: Project file not found at $PROJECT_FILE_PATH"
  echo "Please create $PROJECT_FILE_PATH containing your Google Cloud project ID."
  return 1 # Return 1 as we are sourcing
fi

# 2. Set the default gcloud project configuration
PROJECT_ID_FROM_FILE=$(cat "$PROJECT_FILE_PATH")
echo "Setting gcloud config project to: $PROJECT_ID_FROM_FILE"

# Adding --quiet; set -e will handle failure if the project doesn't exist or access is denied
gcloud config set project "$PROJECT_ID_FROM_FILE" --quiet

# 3. Export PROJECT_ID (Get from config to confirm it was set correctly)
export PROJECT_ID=$(gcloud config get project)
echo "Exported PROJECT_ID=$PROJECT_ID"

# 4. Export PROJECT_NUMBER
export PROJECT_NUMBER=$(gcloud projects describe ${PROJECT_ID} --format="value(projectNumber)")
echo "Exported PROJECT_NUMBER=$PROJECT_NUMBER"

# 5. Export SERVICE_ACCOUNT_NAME (Default Compute Service Account)
export SERVICE_ACCOUNT_NAME=$(gcloud compute project-info describe --format="value(defaultServiceAccount)")
echo "Exported SERVICE_ACCOUNT_NAME=$SERVICE_ACCOUNT_NAME"


# 6. Export GOOGLE_CLOUD_PROJECT (Often used by client libraries)
# This is usually the same as PROJECT_ID
export GOOGLE_CLOUD_PROJECT="$PROJECT_ID"
echo "Exported GOOGLE_CLOUD_PROJECT=$GOOGLE_CLOUD_PROJECT"

# 9. Export GOOGLE_GENAI_USE_VERTEXAI
export GOOGLE_GENAI_USE_VERTEXAI="TRUE"
echo "Exported GOOGLE_GENAI_USE_VERTEXAI=$GOOGLE_GENAI_USE_VERTEXAI"

# 10. Export REGION and GOOGLE_CLOUD_LOCATION
export REGION="us-central1"
export GOOGLE_CLOUD_LOCATION="$REGION"
echo "Exported REGION=$REGION"
echo "Exported GOOGLE_CLOUD_LOCATION=$GOOGLE_CLOUD_LOCATION"


export TOOLBOX_VERSION=0.10.0
echo "Exported TOOLBOX_VERSION=$TOOLBOX_VERSION"

# -- Cloud SQL (Librarium of Knowledge) --
export DB_INSTANCE_NAME="summoner-librarium-db"
export DB_NAME="familiar_grimoire"
export DB_USER="summoner"
export DB_PASSWORD="1234qwer"
echo "Exported DB_INSTANCE_NAME=$DB_INSTANCE_NAME"
echo "Exported DB_NAME=$DB_NAME"
echo "Exported DB_USER=$DB_USER"
echo "Exported DB_PASSWORD=$DB_PASSWORD"

export FAKE_API_SERVICE_NAME="nexus-of-whispers-api"
echo "Exported FAKE_API_SERVICE_NAME=$FAKE_API_SERVICE_NAME"

export API_SERVER_URL=$(gcloud run services describe $FAKE_API_SERVICE_NAME --format 'value(status.url)' --region $REGION 2>/dev/null || true)
echo "Exported API_SERVER_URL=$API_SERVER_URL"

export FIRE_URL=$(gcloud run services describe fire-familiar --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)
echo "Exported FIRE_URL=$FIRE_URL"

export WATER_URL=$(gcloud run services describe water-familiar --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)
echo "Exported WATER_URL=$WATER_URL"

export EARTH_URL=$(gcloud run services describe earth-familiar --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)
echo "Exported EARTH_URL=$EARTH_URL"

export DB_TOOLS_URL=$(gcloud run services describe toolbox --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)
echo "Exported DB_TOOLS_URL=$DB_TOOLS_URL"

# Note: If the following gcloud commands fail, the variable will be set to just "/sse".
export API_TOOLS_URL=$(gcloud run services describe api-tools-mcp --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)/sse
echo "Exported API_TOOLS_URL=$API_TOOLS_URL"

export FUNCTION_TOOLS_URL=$(gcloud run services describe general-tools-mcp --platform managed --region $REGION --format 'value(status.url)' 2>/dev/null || true)/sse
echo "Exported FUNCTION_TOOLS_URL=$FUNCTION_TOOLS_URL"

export A2A_BASE_URL="-${PROJECT_NUMBER}.${REGION}.run.app"
echo "Exported A2A_BASE_URL=$A2A_BASE_URL"

# ===================================================================

echo ""
echo "--- Environment setup complete ---"