# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

RUN apt-get update && apt-get install -y sqlite3

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

RUN sqlite3 marketplace.db < schema.sql

# Expose Flask’s port
EXPOSE 5001

# Run the app
CMD ["python", "main.py"]