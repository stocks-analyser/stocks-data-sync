FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1



# Set working directory
WORKDIR /app

# Install pandas
RUN pip install --no-cache-dir pandas

# Copy only requirements.txt to leverage Docker cache
COPY ../requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY src/ /app

# Define default command
ENTRYPOINT ["python", "data-sync.py"]