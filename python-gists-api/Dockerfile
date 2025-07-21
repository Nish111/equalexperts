# Dockerfile for Python Gists API
# Based on Python 3.11 slim image for a lightweight container

FROM python:3.11-slim

# Create a non-root user
RUN useradd -m appuser

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy app code
COPY . .

# Set PATH to include user-level pip installs
ENV PATH="/root/.local/bin:$PATH"

# Use non-root user
USER appuser

# Expose port (optional but good practice)
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
