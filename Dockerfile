# Use the official Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables for non-interactive mode
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip python3-dev build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the Django project files to the containers
COPY . /app

# Install 
RUN pip3 install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000"]
