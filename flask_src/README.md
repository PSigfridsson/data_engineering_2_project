#Run these commands to start the flask container
- sudo docker build --tag flask-docker .
- sudo docker run --publish 5000:5000 flask-docker