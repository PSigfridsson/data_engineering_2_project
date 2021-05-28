# syntax=docker/dockerfile:1
FROM python:3.8-buster
COPY consumerQ1.py .
COPY consumerQ2.py .
COPY consumerQ3.py .
COPY consumerQ4.py .
COPY producer.py .
COPY producer_continuous.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt