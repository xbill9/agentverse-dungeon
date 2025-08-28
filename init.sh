
#!/bin/bash

# --- Function for error handling ---
handle_error() {
  echo "Error: $1"
  exit 1
}

# --- Part 1: Set Google Cloud Project ID ---
PROJECT_FILE="$HOME/project_id.txt"
echo "--- Setting Google Cloud Project ID File ---"

read -p "Please enter your Google Cloud project ID: " user_project_id

if [[ -z "$user_project_id" ]]; then
  handle_error "No project ID was entered."
fi

echo "You entered: $user_project_id"
echo "$user_project_id" > "$PROJECT_FILE"

if [[ $? -ne 0 ]]; then
  handle_error "Failed saving your project ID: $user_project_id."
fi
echo "Successfully saved project ID."

cd ~/agentverse-dungeon
source ./set_env.sh

gcloud config set project $(cat ~/project_id.txt) 

gcloud services enable \
    sqladmin.googleapis.com \
    storage.googleapis.com \
    aiplatform.googleapis.com \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com \
    iam.googleapis.com \
    compute.googleapis.com \
    cloudresourcemanager.googleapis.com \
    secretmanager.googleapis.com

echo $REPO_NAME

 
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=$REGION \
    --description="Repository for Agentverse agents"

# --- Grant Core Data Permissions ---
gcloud projects add-iam-policy-binding $PROJECT_ID \
 --member="serviceAccount:$SERVICE_ACCOUNT_NAME" \
 --role="roles/storage.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/aiplatform.user"

# --- Grant Deployment & Execution Permissions ---
gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/cloudbuild.builds.editor"

gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/artifactregistry.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/iam.serviceAccountUser"

gcloud projects add-iam-policy-binding $PROJECT_ID  \
--member="serviceAccount:$SERVICE_ACCOUNT_NAME"  \
--role="roles/logging.logWriter"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}" \
  --role="roles/monitoring.metricWriter"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}" \
  --role="roles/secretmanager.secretAccessor"



echo "--- Setup complete ---"
exit 0
