FROM python:3
WORKDIR /app

RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python3 -m venv venv && \
    /bin/bash -c "source venv/bin/activate" && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/bash", "-c", "sleep 30  && tail -f /dev/null"]
