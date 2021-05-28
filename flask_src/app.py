from flask import Flask, render_template, jsonify, request
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_topxlang')
def topxlang():
	topx = request.args.get('topx')

	mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
	db = mongoClient["Github_statistics"]
	col = db["language_count"]

	result = []
	for x in col.aggregate([{'$sort': {'count': -1}}, {'$limit': int(topx)}]):
		result.append((x['language'], x['count']))

	return jsonify({'top10': result})

@app.route('/_topxcommits')
def topxcommits():
	topx = request.args.get('topx')

	mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
	db = mongoClient["Github_statistics"]
	col = db["repo_commit_count"]

	result = []
	for x in col.aggregate([{'$sort': {'count': -1}}, {'$limit': int(topx)}]):
		result.append((x['repo'], x['count']))

	return jsonify({'top10': result})

@app.route('/_topxunittest')
def topxunittest():
	topx = request.args.get('topx')

	mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
	db = mongoClient["Github_statistics"]
	col = db["unit_test_count"]

	result = []
	for x in col.aggregate([{'$sort': {'count': -1}}, {'$limit': int(topx)}]):
		result.append((x['language'], x['count']))

	return jsonify({'top10': result})

@app.route('/_topxunittestci')
def topxunittestci():
	topx = request.args.get('topx')

	mongoClient = pymongo.MongoClient("mongodb://mongo:27017/")
	db = mongoClient["Github_statistics"]
	col = db["unit_test_and_ci_count"]

	result = []
	for x in col.aggregate([{'$sort': {'count': -1}}, {'$limit': int(topx)}]):
		result.append((x['language'], x['count']))

	return jsonify({'top10': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
