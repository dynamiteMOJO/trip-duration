# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Copy the required files and directory into the container at /app
COPY service.py /app/service.py
COPY model.joblib /app/model.joblib
COPY src/ /app/src/

# Copy files from S3 inside docker
# RUN mkdir /app/models
# RUN aws s3 cp s3://creditcard-project/models/model.joblib /app/models/model.joblib

# EXPOSE 8080

# start the server
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8080"]