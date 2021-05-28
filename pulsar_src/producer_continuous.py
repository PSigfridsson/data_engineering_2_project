import pulsar
import requests
import json
import time
import datetime
from datetime import timedelta

def main():
	client = pulsar.Client('pulsar://pulsar:6650')
	producer = client.create_producer('Maintopic')

	i = 0
	username, token, _ = get_next_token(i)
	start = datetime.datetime.strptime("2020-05-27", "%Y-%m-%d")
	end = datetime.datetime.strptime("2021-05-27", "%Y-%m-%d")
	delta = timedelta(days=1)

	while start <= end:
		repo_url = 'https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), 1)
		r = api_request(repo_url, username, token)

		while True:
			try:
				for item in r.json()['items']:
					producer.send('{} {} {}'.format(item['full_name'], item['language'], item['url']).encode('utf-8'))

				next_url = find_next_url(r)
				if next_url == None:
					break

				username, token, i = get_random_token(i)
				i+=1
				r = api_request(next_url, username, token)

			except:
				print('Sleep for 60s')
				time.sleep(60)
				i+=1


def api_request(url, username, token):
	r = requests.get(url, auth=(username, token), headers = {"link":"text"})
	return r

def find_next_url(req):
	links = req.headers['link']
	
	if(links.find('rel="next"') == -1):
		return None

	links_sub = links[:links.find('rel="next"')]
	
	if(links_sub.find('rel="prev"') != -1):
		links_sub = links_sub[links_sub.find('rel="prev"'):]
	
	next_url = links_sub[links_sub.find('<')+1:links_sub.find('>')]

	return next_url

def get_next_token(i):
	token_list = [('AlexisTubulekas', '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'), ('elenafilonova', 'ccec9e791ed01388009a380162f8ad5a9feb9b53'), ('psigfridsson', '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'), ('WSandkvist', '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')]
	#if we've reached the end of token_list reset index i = 0
	if i > (len(token_list)-1):
		i = 0

	next_token_pair = token_list[i]
	username = next_token_pair[0]
	token = next_token_pair[1]
	return username,token,i

if __name__ == "__main__":
	main()