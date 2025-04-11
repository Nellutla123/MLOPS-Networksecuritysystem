FROM python:3.10-buster

WORKDIR /app
COPY . /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends awscli python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]



