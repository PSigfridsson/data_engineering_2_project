#!/usr/bin/env python

from pulsar import Function
import requests
import os
import json
import time
import regex as re
import random

class commitsCounter(Function):
    def __init__(self):
        self.commits = "persistent://public/default/q2-output"
    def process(self, input, context):
        tokens = {'elenafilonova': 'ccec9e791ed01388009a380162f8ad5a9feb9b53', 'WSandkvist': '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', 'AlexisTubulekas': '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'}
        username = random.choice(list(tokens))
        token = tokens[username]
        input_split = input.split(' ')
        commits = re.search('\d+$', requests.get('{}'.format(input_split[1] + '/commits?per_page=1'), auth=(username, token)).links['last']['url']).group()
        context.publish(self.commits, '{} {}'.format(input_split[0], commits))
        
        
