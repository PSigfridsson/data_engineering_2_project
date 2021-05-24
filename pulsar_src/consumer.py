import pulsar
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('language_count', subscription_name='lang_count-sub')
# Display message received from producer
while True:
	msg = consumer.receive()
	try:
		print("Received message : '%s'" % msg.data())
		msg_tuple = msg.data().decode('utf-8')
		msg_tuple = msg_tuple[1:]
		msg_tuple = msg_tuple[:-1]
		msg_tuple = tuple(msg_tuple.split(', '))
		socketio.emit('language_count', {'language': msg_tuple[0], 'count': msg_tuple[1]}, namespace='/test')
		# Acknowledge for receiving the message
		consumer.acknowledge(msg)
	except:
		consumer.negative_acknowledge(msg)

# Destroy pulsar client
client.close()