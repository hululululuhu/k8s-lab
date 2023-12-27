#!/bin/bash

# build MySQL pv
echo "Deploying MySQL master and slave config..."
kubectl apply -f mysql-master-config.yaml
kubectl apply -f mysql-slave-config.yaml
echo "MySQL master and slave config deployed."

# build MySQL pv
echo "Deploying MySQL master and slave pv..."
kubectl apply -f mysql-master-pv-claim.yaml
kubectl apply -f mysql-slave-pv-claim.yaml
echo "MySQL master and slave pv deployed."

# build MySQL master-slave
echo "Deploying MySQL master and slave services..."
kubectl apply -f mysql-master-service.yaml
kubectl apply -f mysql-slave-service.yaml
echo "MySQL master and slave services deployed."

# build MySQL master-slave Deployment
echo "Deploying MySQL master and slave deployments..."
kubectl apply -f mysql-master-deployment.yaml
kubectl apply -f mysql-slave-deployment.yaml
echo "MySQL master and slave deployments deployed."

echo "Checking the status of deployments..."

kubectl get deployments
echo "Checking the status of services..."
kubectl get services
