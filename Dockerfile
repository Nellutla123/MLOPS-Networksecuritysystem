FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

# Update and install awscli in one step
RUN apt-get update -y && apt-get install -y awscli

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the app
CMD ["python3", "app.py"]

