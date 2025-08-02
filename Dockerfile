FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Create media directory
RUN mkdir -p src/media

# Expose port
EXPOSE 8000

# Change to src directory and run the application
WORKDIR /app/src
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 