import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('language_count', subscription_name='lang_count_sub')
# Display message received from producer

msg = consumer.receive()
try:
	print("Received message : '%s'" % msg.data())
	msg_tuple = msg.data().decode('utf-8')
	msg_tuple = msg_tuple[1:]
	msg_tuple = msg_tuple[:-1]
	msg_tuple = tuple(msg_tuple.split(', '))
	print("Lang_count_tuple: ", msg_tuple)
	# Acknowledge for receiving the message
	consumer.acknowledge(msg)
except:
	consumer.negative_acknowledge(msg)

# Destroy pulsar client
client.close()