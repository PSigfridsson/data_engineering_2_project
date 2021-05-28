from pulsar import Function
import requests
import json

'''
sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/unittestciCounter.py --classname unittestciCounter.unittestciCounter --inputs persistent://public/default/q3-topic --tenant public --namespace default

Inside docker container:
bin/pulsar-admin functions create --py unittestciCounter.py --classname unittestciCounter.unittestciCounter --inputs persistent://public/default/q3-topic --tenant public --namespace default

--inputs persistent://public/default/q4-output
'''
class unittestciCounter(Function):
    def __init__(self):
        self.unittestci = "persistent://public/default/unit_test_ci_count"

    def process(self, input, context):
        context.incr_counter(input, 1)
        unit_test_ci_count = (input, context.get_counter(input))
        context.publish(self.unittestci, str(unit_test_ci_count))