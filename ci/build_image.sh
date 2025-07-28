#!/bin/bash
#
# Builds docker image and pushes to ECR
#

$(aws ecr get-login --no-include-email --region us-east-1)
docker login -u $GHCR_USER -p $GHCR_TOKEN ghcr.io  # Necessário para imagens base
DOCKER_BUILDKIT=1 docker build --build-arg AWS_SECRET_ID=$AWS_SECRET_ID --ssh default --cache-from $AWS_ECR:latest -t $AWS_ECR:$GITHUB_RUN_ID -t $AWS_ECR:latest -f docker/deploy/Dockerfile .
docker push $AWS_ECR:$GITHUB_RUN_ID
docker push $AWS_ECR:latest