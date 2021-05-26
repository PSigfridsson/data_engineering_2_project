from pulsar import Function
import requests
import json

'''
sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/unittestCounter.py --classname unittestCounter.unittestCounter --inputs persistent://public/default/q3-topic --tenant public --namespace default

'''
class unittestCounter(Function):
    def __init__(self):
        self.unittest = "persistent://public/default/q3-output"

    def process(self, input, context):
        username = 'psigfridsson'
        token = "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"

        input_split = input.split(' ')
        files = requests.get('{}'.format(input_split[1] + '/contents'), auth=(username, token))
        for j in range(len(files.json())):
            if 'test' in files.json()[j]['name']:
                context.incr_counter(input_split[0], 1)
                unit_count = (input_split[0], context.get_counter(input_split[0]))
                context.publish(self.unittest, str(unit_count))
