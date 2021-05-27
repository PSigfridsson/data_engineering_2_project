# syntax=docker/dockerfile:1
FROM python:3.8-buster
COPY consumerQ4.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD ["python3", "consumerQ4.py"]