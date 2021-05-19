from pulsar import Function

class languageCounter(Function):
	def __init__(self):
		self.language_count_topic = "persistent://public/default/language_count"

	def process(self, input, context):
		
		context.incr_counter(self, input, 1)
		lang_count = (input, context.get_counter(input))
		context.publish(self.language_count_topic, lang_count)