import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('DEtopic', subscription_name='DE-sub')
# Display message received from producer
msg = consumer.receive()

try:
	print("Received message : '%s'" % msg.data())
	# Acknowledge for receiving the message
	consumer.acknowledge(msg)
except:
	consumer.negative_acknowledge(msg)

# Destroy pulsar client
client.close()