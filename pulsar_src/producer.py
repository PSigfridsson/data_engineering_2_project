import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Create a producer on the topic that consumer can subscribe to
producer = client.create_producer('DEtopic')
# Send a message to consumer
producer.send('Python'.encode('utf-8'))
# Destroy pulsar
client.close()