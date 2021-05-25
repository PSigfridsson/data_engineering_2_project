from pulsar import Function
import pymongo

'''

sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/languageCounter.py --classname languageCounter.languageCounter --inputs persistent://public/default/q1-topic --tenant public --namespace default

'''
class languageCounter(Function):
	def __init__(self):
		self.language_count_topic = "persistent://public/default/language_count"

	def process(self, input, context):
		context.incr_counter(input, 1)
		lang_count = (input, context.get_counter(input))

		mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
		db = mongoClient["Github_statistics"]
		col = db["language_count"]

		key = {'language': input_tuple[0]}
		value = {'$set': {'count': int(input_tuple[1])}}
		col.update_one(key, value, upsert=True)

		#context.publish(self.language_count_topic, str(lang_count))
