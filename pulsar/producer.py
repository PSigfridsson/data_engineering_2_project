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
end = datetime.datetime.strptime("2021-05-24", "%Y-%m-%d")
delta = timedelta(days=1)

# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('Maintopic')
# getting the data
while start <= end:
    print(username, token)
    print(start)
    print('i =', i)
    try: 
        for page in range(1,11):
            repo = requests.get('https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), page), auth=(username, token))
            for j in range(len(repo.json()['items'])):
                # Send a message to topic
                producer.send('{} {} {}'.format(repo.json()['items'][j]['full_name'], repo.json()['items'][j]['language'], repo.json()['items'][j]['url']).encode('utf-8'))
    except:
        time.sleep(60)

    start += delta
        
    if i == 1:
        username = 'elenafilonova'
        token = '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'
        i = 0
    else:
        username = 'elenafilonova'
        token = 'ccec9e791ed01388009a380162f8ad5a9feb9b53'
        i += 1
    
# Destroy pulsar client
client.close()
