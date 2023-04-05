# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements_api.txt

# Set the environment variable for the Flask app
ENV FLASK_APP=api.py

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the command to start the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
