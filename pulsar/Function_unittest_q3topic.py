#!/usr/bin/env python

from pulsar import Function
import requests
import os
import json
import time

class unittestCounter(Function):
    def __init__(self):
        self.unittest = "persistent://public/default/q3-output"
    def process(self, input, context):
        username = 'elenafilonova'
        token = os.environ.get("ccec9e791ed01388009a380162f8ad5a9feb9b53")
        input_split = input.split(' ')
        files = requests.get('{}'.format(input_split[1] + '/contents'), auth=(username, token))
        for j in range(len(files.json())):
            if 'test' in files.json()[j]['name']:
                context.publish(self.unittest, '{}'.format(input_split[0]))
