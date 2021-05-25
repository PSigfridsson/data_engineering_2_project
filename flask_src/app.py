from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_top10lang')
def top10lang():
	return jsonify({'top10': [('Python', 1), ('Java', 2)]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
