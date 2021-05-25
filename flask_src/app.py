from flask import Flask, render_template, jsonify, request
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_top10lang')
def top10lang():
	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = mongoClient["Github_statistics"]
	col = db["language_count"]

	result = []
	for x in col.aggregate([{'$sort': {'count': 1}}, {'$limit': 10}]):
		result.append((x['language'], x['count']))
		
	return jsonify({'top10': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
