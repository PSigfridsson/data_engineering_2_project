import pulsar
import requests
import json
import time
import datetime
from datetime import timedelta
i = 0
username = 'elenafilonova'
token = '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'
start = datetime.datetime.strptime("2020-05-25", "%Y-%m-%d")
print(username, token)
end = datetime.datetime.strptime("2021-05-24", "%Y-%m-%d")
delta = timedelta(days=1)

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('Maintopic')
# getting the data
while start <= end:
    try:
        for page in range(1,11):
            repo = requests.get('https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), page), auth=(username, token))
            for i in range(len(repo.json()['items'])):
                # Send a message to consumer
                producer.send('{} {} {}'.format(repo.json()['items'][i]['full_name'], repo.json()['items'][i]['language'], repo.json()['items'][i]['url']).encode('utf-8'))

        start += delta
        
        if i == 1:
            username = 'elenafilonova'
            token = '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'
            i = 0
            print(username, token)
        else:
            username = 'elenafilonova'
            token = 'ccec9e791ed01388009a380162f8ad5a9feb9b53'
            i += 1
            print(username, token)
    
    except:
        time.sleep(60)

# Destroy pulsar client
client.close()
