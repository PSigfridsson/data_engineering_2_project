# syntax=docker/dockerfile:1
FROM python:latest
COPY producer.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python3", "producer.py"]