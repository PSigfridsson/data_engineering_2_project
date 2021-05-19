from pulsar import Function

class languageCounter(Function):
	def process(self, context, input):
		context.incr_counter(self, input, 1)

		return input