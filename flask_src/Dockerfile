# syntax=docker/dockerfile:1

FROM python:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install flask
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]