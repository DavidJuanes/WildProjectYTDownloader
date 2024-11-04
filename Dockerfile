
FROM python:3.11-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/start.py .

CMD ["python", "start.py"]

