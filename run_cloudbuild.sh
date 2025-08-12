#!/bin/bash
nohup gcloud builds submit --config cloudbuild.yaml \
  --substitutions=_REGION="$REGION",_REPO_NAME="$REPO_NAME",_SERVICE_NAME="agentverse-dungeon" \
  "$@" > cloudbuild.log 2>&1 &
echo "Cloud Build job submitted in the background. Output redirected to cloudbuild.log"