FROM python:3.11-bookworm

FROM ubuntu:20.04

WORKDIR /app

ENV DISPLAY=:0

RUN apt-get update && apt-get install -y firefox && rm -rf /var/lib/apt/lists/

COPY . /app

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["python", "firefox", "main.py"]