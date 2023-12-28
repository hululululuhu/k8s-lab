#!/bin/bash

# setting
IMAGE_NAME="my-python-mysql-app"
REGISTRY_URL="hub.docker.com/v2"
USERNAME="magiwu"
NAMESPACE="default"
YOUR_PASSWORD="wu1056814738"

# build docker image
docker build -t ${IMAGE_NAME} -f deployment/Dockerfile .
echo "build docker image succeed"

# docker login
docker login
echo "docker login succeed"

# push docker image
docker tag ${IMAGE_NAME} ${USERNAME}/${IMAGE_NAME}:latest
docker push ${USERNAME}/${IMAGE_NAME}:latest
echo "push docker image succeed"

# deploy to k8s
kubectl config use-context minikube
kubectl create namespace ${NAMESPACE} --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -f deployment/my-api.yaml -n ${NAMESPACE}
echo "deploy k8s pod succeed"

# remove remote image
docker rmi ${USERNAME}/${IMAGE_NAME}:latest
echo "remove docker image succeed"