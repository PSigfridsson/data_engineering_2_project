# syntax=docker/dockerfile:1
FROM python:latest
COPY consumerQ2.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python3", "consumerQ2.py"]