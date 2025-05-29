FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only requirements.txt to leverage Docker cache
COPY . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files

# Define default command
ENTRYPOINT ["python", "data-sync.py"]