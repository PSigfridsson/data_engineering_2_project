#!/usr/bin/env python

from pulsar import Function
import requests
import os
import json
import time
import regex as re

class commitsCounter(Function):
    def __init__(self):
        self.commits = "persistent://public/default/q2-output"
    def process(self, input, context):
        username = 'elenafilonova'
        token = os.environ.get("ccec9e791ed01388009a380162f8ad5a9feb9b53")
        input_split = input.split(' ')
        commits = re.search('\d+$', requests.get('{}'.format(input_split[1] + '/commits?per_page=1'), auth=(username, token)).links['last']['url']).group()
        context.publish(self.commits, '{} {}'.format(input_split[0], commits))
        time.sleep(2)
