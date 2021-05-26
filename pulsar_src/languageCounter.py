from pulsar import Function

'''

sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/languageCounter.py --classname languageCounter.languageCounter --inputs persistent://public/default/q1-topic --tenant public --namespace default

'''
class languageCounter(Function):
	def __init__(self):
		self.language_count_topic = "persistent://public/default/language_count"

	def process(self, input, context):
		key = "langcount_"+input
		context.incr_counter(key, 1)
		lang_count = (input, context.get_counter(key))
		context.publish(self.language_count_topic, str(lang_count))
