# Build stage
FROM python:3.13-slim-bullseye AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Create and activate virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.13-slim-bullseye

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copy only necessary files
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Create required directories
RUN mkdir -p uploads converted

EXPOSE 5000

CMD ["python3", "app.py"]