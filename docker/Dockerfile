FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pandas
RUN pip install --no-cache-dir pandas

# Set working directory
WORKDIR /app

# Copy application files
COPY . /app

# Define default command
CMD ["python", "data-sync.py"]