import pulsar
import requests
import os
import json
import time
username = 'elenafilonova'
token = os.environ.get("ccec9e791ed01388009a380162f8ad5a9feb9b53")
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('Maintopic')
# getting the data
repo = requests.get('https://api.github.com/search/repositories?q=pushed:"2021-05-14"&per_page=100', auth=(username, token))
for i in range(len(repo.json()['items'])):
    # Send a message to consumer
    producer.send('{} {} {}'.format(repo.json()['items'][i]['full_name'], repo.json()['items'][i]['language'], repo.json()['items'][i]['url']).encode('utf-8'))
# Destroy pulsar client
client.close()
