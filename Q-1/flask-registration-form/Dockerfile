# Use official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
