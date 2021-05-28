from pulsar import Function

'''
sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/unittestCounter.py --classname unittestCounter.unittestCounter --inputs persistent://public/default/q3-topic --tenant public --namespace default

Inside docker container:
bin/pulsar-admin functions create --py unittestCounter.py --classname unittestCounter.unittestCounter --inputs persistent://public/default/q3-topic --tenant public --namespace default

--inputs persistent://public/default/q3-output
'''
class unittestCounter(Function):
    def __init__(self):
        self.unittest = "persistent://public/default/unit_test_count"

    def process(self, input, context):
        context.incr_counter(input, 1)
        unit_test_count = (input, context.get_counter(input))
        context.publish(self.unittest, str(unit_test_count))