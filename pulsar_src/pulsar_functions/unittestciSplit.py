from pulsar import Function
import requests
import json
import random

class unittestciSplit(Function):
    def __init__(self):
        self.unittests = "persistent://public/default/q3-output"
        self.cis = "persistent://public/default/q4-output"

    def process(self, input, context):
        tokens = {'elenafilonova': 'ccec9e791ed01388009a380162f8ad5a9feb9b53', 'WSandkvist': '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', 'AlexisTubulekas': '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', 'psigfridsson': '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'}
        username = random.choice(list(tokens))
        token = tokens[username]
        input_split = input.split(' ')
        test_files = []
        try:
            files = requests.get(input_split[1] + '/contents', auth=(username, token))
            for j in range(len(files.json())):
                try:
                    test_files.append(files.json()[j]['name'].lower())
                except:
                    pass
        except:
            pass
            
        if ('test' in test_files) or ('tests' in test_files):
            context.publish(self.unittests, '{}'.format(input_split[0]))
            if ('.travis.yml' in test_files) or ('.circleci' in test_files) or ('jenkins' in test_files):
                context.publish(self.cis, '{}'.format(input_split[0]))