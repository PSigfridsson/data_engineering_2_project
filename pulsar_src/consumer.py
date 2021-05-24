import pulsar
import pymongo
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
	
	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = mongoClient["Github_statistics"]
	col = db["language_count"]

	key = {'language': msg_tuple[0]}
	value = {'$set': {'count': msg_tuple[1]}}
	col.update_one(key, value, upsert=True)
	# Acknowledge for receiving the message
	consumer.acknowledge(msg)
except:
	consumer.negative_acknowledge(msg)

# Destroy pulsar client
client.close()