from pulsar import Function

'''
Splitting initial repo data into Q1-Q4 topics

sudo bin/pulsar-admin functions create --py ~/data_engineering_2_project/pulsar_src/topicSplit.py --classname topicSplit.topicSplit --inputs persistent://public/default/Maintopic --tenant public --namespace default

Inside docker container:
bin/pulsar-admin functions create --py topicSplit.py --classname topicSplit.topicSplit --inputs persistent://public/default/Maintopic --tenant public --namespace default

'''
class topicSplit(Function):
    def __init__(self):
        self.q1_topic = "persistent://public/default/q1-topic"
        self.q2_topic = "persistent://public/default/q2-topic"
        self.q3_q4_topic = "persistent://public/default/q3-q4-topic"

    def process(self, string, context):
        # splitting the input
        split_string = string.split(' ')
        context.publish(self.q1_topic, split_string[1])
        context.publish(self.q2_topic, '{} {}'.format(split_string[0], split_string[2]))
        context.publish(self.q3_q4_topic, '{} {}'.format(split_string[1], split_string[2]))
