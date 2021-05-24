from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


import pulsar
from pulsar import ConsumerType
# Create a pulsar client by supplying ip address and port
client = pulsar.Client('pulsar://localhost:6650')
# Subscribe to a topic and subscription
consumer = client.subscribe('q1-topic', subscription_name='q1-sub', consumer_type=ConsumerType.Shared)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#Consumer thread
thread = Thread()
thread_stop_event = Event()

language_count = {}

def pulsarStatistics():
	while not thread_stop_event.isSet():
		msg = consumer.receive()
		try:
			msg_str = msg.data().decode('utf-8')
			print("Received message : '%s'" % msg_str)

			if msg_str not in list(language_count.keys()):
			    language_count[msg_str] = 1
			else:
			    language_count[msg_str] += 1

			#msg_tuple = msg.data().decode('utf-8')
			#msg_tuple = msg_tuple[1:]
			#msg_tuple = msg_tuple[:-1]
			#msg_tuple = tuple(msg_tuple.split(', '))
			socketio.emit('lang_count_dict', {'lang_count_dict': language_count}, namespace='/test')
			#socketio.emit('language_count', {'language': msg_tuple[0], 'count': msg_tuple[1]}, namespace='/test')
			# Acknowledge for receiving the message
			consumer.acknowledge(msg)
		except:
			consumer.negative_acknowledge(msg)
	# Destroy pulsar client
	client.close()

@app.route('/')
def index():
	#only by sending this page first will the client be connected to the socketio instance
	return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
	# need visibility of the global thread object
	global thread
	print('Client connected')

	if not thread.isAlive():
		print("Starting Thread")
		thread = socketio.start_background_task(pulsarStatistics)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected')


if __name__ == '__main__':
	socketio.run(app)
