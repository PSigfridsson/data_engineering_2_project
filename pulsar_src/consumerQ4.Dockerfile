# syntax=docker/dockerfile:1
FROM python:latest
COPY consumerQ4.py .
RUN pip3 install -r requirements.txt
CMD ["python3", "consumerQ4.py"]