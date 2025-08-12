#!/bin/bash
nohup gcloud builds submit --config cloudbuild.yaml "$@" > cloudbuild.log 2>&1 &
echo "Cloud Build job submitted in the background. Output redirected to cloudbuild.log"
