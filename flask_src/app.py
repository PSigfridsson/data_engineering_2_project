from flask import Flask, render_template, url_for, copy_current_request_context

app = Flask(__name__)

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
