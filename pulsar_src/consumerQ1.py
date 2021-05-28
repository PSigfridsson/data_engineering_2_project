import pulsar
from pulsar import ConsumerType
import pymongo

client = pulsar.Client('pulsar://pulsar:6650')
consumer = client.subscribe('language_count', subscription_name='q1-sub', consumer_type=ConsumerType.Shared)

while True:
	msg = consumer.receive()
	try:
		print("Received message : '%s'" % msg.data())
		msg_tuple = msg.data().decode('utf-8')
		msg_tuple = msg_tuple[1:]
		msg_tuple = msg_tuple[:-1]
		msg_tuple = tuple(msg_tuple.split(', '))
		input_tuple = (msg_tuple[0][1:][:-1], msg_tuple[1])
		print("Lang_count_tuple: ", input_tuple)
		
		mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
		db = mongoClient["Github_statistics"]
		col = db["language_count"]

		key = {'language': input_tuple[0]}
		value = {'$set': {'count': int(input_tuple[1])}}
		col.update_one(key, value, upsert=True)
		# Acknowledge for receiving the message
		consumer.acknowledge(msg)
	except:
		consumer.negative_acknowledge(msg)

# Destroy pulsar client
client.close()