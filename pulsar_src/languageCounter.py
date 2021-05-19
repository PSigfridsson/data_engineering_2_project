from pulsar import Function


'''

sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/languageCounter.py --classname languageCounter.languageCounter --inputs persistent://public/default/DEtopic --tenant public --namespace default

'''
class languageCounter(Function):
	def __init__(self):
		self.language_count_topic = "persistent://public/default/language_count"

	def process(self, input, context):
		context.incr_counter(input, 1)
		lang_count = (input, context.get_counter(input))
		context.publish(self.language_count_topic, str(lang_count))