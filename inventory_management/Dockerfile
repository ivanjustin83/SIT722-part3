# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install SSL certificates and openssl
RUN apt-get update && apt-get install -y ca-certificates openssl

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]