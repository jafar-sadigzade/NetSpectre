# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    sudo \
    nmap \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /app/

# Create a non-root user
RUN adduser --disabled-password --gecos '' django_user
RUN mkdir -p /app/staticfiles
RUN chown -R django_user:django_user /app

# Switch to the non-root user
USER django_user

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "netspectre.wsgi:application"]
