# Use an official Python image as base
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY app.py .
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5200

# Start the Flask application
CMD ["python", "app.py"]
