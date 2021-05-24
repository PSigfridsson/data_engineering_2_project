import pulsar
from pulsar import ConsumerType
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('q3-output', subscription_name='DE-sub', consumer_type=ConsumerType.Shared)

unittest_count = {}

# Display message received from producer
while True:
    msg = consumer.receive()
    try:
        msg_str = msg.data().decode('utf-8')
        if msg_str not in list(unittest_count.keys()):
            unittest_count[msg_str] = 1
        else:
            unittest_count[msg_str] += 1
        #print("Received message : '%s'" % msg_str)
        print('Top languages with unittests.\nCurrent count:')
        for i in sorted(unittest_count.items(), key=lambda x: x[1], reverse=True):
            print(i[0], '\t', i[1])


        # Acknowledge for receiving the message
        consumer.acknowledge(msg)
    except:
        consumer.negative_acknowledge(msg)
        
# Destroy pulsar client
client.close()
