# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the wheel and other contents into the container at /app
COPY . /app

# List contents of /app for debugging
RUN ls -la /app

# Check architecture and install wheel conditionally
RUN if [ "$(uname -m)" = "x86_64" ]; then \
        pip install -r requirements-amd64.txt; \
    else \
        pip install -r requirements-arm64.txt; \
    fi

# Make port 8501 available to the world outside this container
EXPOSE 8501

# HEALTHCHECK to ensure the app is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Define environment variable
ENV NAME World

# Run app.py when the container launches
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=localhost"]
