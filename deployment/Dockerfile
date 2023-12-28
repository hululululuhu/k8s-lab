FROM python:3.8-slim

RUN pip install mysql-connector-python

RUN pip install flask

ENV PYTHONUNBUFFERED=1
# Set the working directory
WORKDIR /opt/k8s-lab

# Copy all files from the k8s-lab directory into the image
ADD . /opt/k8s-lab

