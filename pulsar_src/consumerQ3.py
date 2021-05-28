import pulsar
from pulsar import ConsumerType
import pymongo

client = pulsar.Client('pulsar://pulsar:6650')
consumer = client.subscribe('unit_test_count', subscription_name='q3-sub', consumer_type=ConsumerType.Shared)

mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
db = mongoClient["Github_statistics"]
col = db["unit_test_count"]

while True:
	msg = consumer.receive()
	try:
		print("Received message : '%s'" % msg.data())
		msg_tuple = msg.data().decode('utf-8')
		msg_tuple = msg_tuple[1:]
		msg_tuple = msg_tuple[:-1]
		msg_tuple = tuple(msg_tuple.split(', '))
		input_tuple = (msg_tuple[0][1:][:-1], int(msg_tuple[1]))
		print("unit_count_tuple: ", input_tuple)

		key = {'language': input_tuple[0]}
		value = {'$set': {'count': input_tuple[1]}}
		col.update_one(key, value, upsert=True)
		consumer.acknowledge(msg)
	except:
		consumer.negative_acknowledge(msg)
		
# Destroy pulsar client
client.close()