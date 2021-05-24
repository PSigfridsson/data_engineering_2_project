#!/usr/bin/env python

from pulsar import Function

# Splitting initial repo data into Q1-Q4 topics

class topics_split(Function):
    def __init__(self):
        self.q1_topic = "persistent://public/default/q1-topic"
        self.q3_topic = "persistent://public/default/q3-topic"

    def process(self, string, context):
        # splitting the input
        split_string = string.split(' ')
        context.publish(self.q1_topic, split_string[1])
        context.publish(self.q3_topic, '{} {}'.format(split_string[1], split_string[2]))
