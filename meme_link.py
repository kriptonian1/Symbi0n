import random

#don't change https://memes.blademaker.tv/api?lang=en
#https://memes.blademaker.tv/api/<subreddit>

def meme_links():
	links = ['https://memes.blademaker.tv/api?lang=en','https://memes.blademaker.tv/api/dankmemes','https://memes.blademaker.tv/api/memes/','https://memes.blademaker.tv/api/wholesomememes/','https://memes.blademaker.tv/api/okbuddyretard/',]
	url = random.choice(links)
	
	return url