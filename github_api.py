import requests
import json
import time
import datetime
from datetime import timedelta
from random import randrange

def main():
	i = 0
	username = 'AlexisTubulekas'
	token = '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'
	start = datetime.datetime.strptime("2021-05-24", "%Y-%m-%d")
	end = datetime.datetime.strptime("2021-05-24", "%Y-%m-%d")
	delta = timedelta(days=1)

	while start <= end:
		#print(start)

		#r = requests.get('https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), 1), auth=(username, token), headers = {"link":"text"})
		my_url = 'https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), 1)
		r = api_request(my_url,username,token)

		#try:
		while True:

			try:

				for j in range(len(r.json()['items'])):
					#Send a message to topic, insert code here
		 			print('{} {} {}'.format(r.json()['items'][j]['full_name'], r.json()['items'][j]['language'], r.json()['items'][j]['url']).encode('utf-8'))

		 		# get the url of the next page
				next_url = find_next_url(r)
				# If there is no next page, break while loop
				if next_url == None:
					break
				
				username,token,i = get_random_token(i)
				i+=1
				#update the current repo based on existing next_url
				r = api_request(next_url,username,token)
				#r = requests.get(next_url, auth=(username, token))
				
			except:
				print('Sleep for 60s')
				time.sleep(60)
				i+=1

		start += delta


def get_random_token(i):
	# list of all available usernames and tokens
	token_list = [('AlexisTubulekas','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'),('AlexisTubulekas','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'),('elenafilonova','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'),('elenafilonova','ccec9e791ed01388009a380162f8ad5a9feb9b53')]
	#if we've reached the end of token_list reset index i = 0
	if i > (len(token_list)-1):
		i = 0
	# choose next username and token pair
	random_token_pair = token_list[i]
	username = random_token_pair[0]
	token = random_token_pair[1]
	return username,token,i

def api_request(url, username, token):
	r = requests.get(url, auth=(username, token), headers = {"link":"text"})
	return r

def find_next_url(req):
	links = req.headers['link']
	#print('links: ',links)
	
	if(links.find('rel="next"') == -1):
		return None

	links_sub = links[:links.find('rel="next"')]
	
	if(links_sub.find('rel="prev"') != -1):
		links_sub = links_sub[links_sub.find('rel="prev"'):]
	
	next_url = links_sub[links_sub.find('<')+1:links_sub.find('>')]
	#print(next_url)
	return next_url

if __name__ == "__main__":
	main()
	print('done')
