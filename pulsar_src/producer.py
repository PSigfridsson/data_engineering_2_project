import pulsar
import requests
import os
import json

username = 'psigfridsson'
token = "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"

client = pulsar.Client('pulsar://mongo:6650')
producer = client.create_producer('Maintopic')

repo = requests.get('https://api.github.com/search/repositories?q=pushed:"2021-05-14"&per_page=100', auth=(username, token))
for i in range(len(repo.json()['items'])):
    # Send a message to consumer
    producer.send('{} {} {}'.format(repo.json()['items'][i]['full_name'], repo.json()['items'][i]['language'], repo.json()['items'][i]['url']).encode('utf-8'))

#producer.send('Python'.encode('utf-8'))
# Destroy pulsar
client.close()