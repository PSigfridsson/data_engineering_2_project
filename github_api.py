import requests
import json
import time
import datetime
from datetime import timedelta
#hej
def main():
	i = 0
	username = 'AlexisTubulekas'
	token = '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'
	start = datetime.datetime.strptime("2020-05-25", "%Y-%m-%d")
	end = datetime.datetime.strptime("2021-05-24", "%Y-%m-%d")
	delta = timedelta(days=1)

	while start <= end:
		print(username, token)
		print(start)
		print('i =', i)

		r = requests.get('https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), 10), auth=(username, token), headers = {"link":"text"})
		# Can return null - r.headers['link']
		next_url = find_next_url(r)
		print(next_url)
		try:
			next_url = find_next_url(r)
			print(next_url)
		except:
			print("No link header")

		break

		# try:
		# 	for page in range(1,11):
		# 		repo = requests.get('https://api.github.com/search/repositories?q=pushed:"{}"&per_page=100&page={}'.format(start.strftime("%Y-%m-%d"), page), auth=(username, token))
		# 		for j in range(len(repo.json()['items'])):
		# 			# Send a message to topic
		# 			print('{} {} {}'.format(repo.json()['items'][j]['full_name'], repo.json()['items'][j]['language'], repo.json()['items'][j]['url']).encode('utf-8'))
		# except:
		# 	print("SLEEEEEEEPPPPPIIIINNGGGG :)")
		# 	time.sleep(60)

		start += delta
			
		# if i == 1:
		# 	username = 'AlexisTubulekas'
		# 	token = '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'
		# 	i = 0
		# else:
		# 	username = 'AlexisTubulekas'
		# 	token = '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'
		# 	i += 1

def find_next_url(req):
	links = req.headers['link']
	
	if(links.find('rel="next"') == -1):
		return None

	links_sub = links[:links.find('rel="next"')]
	
	if(links_sub.find('rel="prev"') != -1):
		links_sub = links_sub[links_sub.find('rel="prev"'):]
	
	next_url = links_sub[links_sub.find('<')+1:links_sub.find('>')]

	return next_url

if __name__ == "__main__":
	main()
