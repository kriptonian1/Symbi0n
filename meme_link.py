import random

#don't change https://memes.blademaker.tv/api?lang=en
#https://memes.blademaker.tv/api/<subreddit>

def meme_links():
	links = ['https://memes.blademaker.tv/api?lang=en','https://memes.blademaker.tv/api/dankmemes','https://memes.blademaker.tv/api/funny','https://memes.blademaker.tv/api/madlad',
  'https://memes.blademaker.tv/api/ComedyCemetery','https://memes.blademaker.tv/api/comedyheaven','https://memes.blademaker.tv/api/technicallythetruth','https://memes.blademaker.tv/api/softwaregore','https://memes.blademaker.tv/api/me_irl','https://memes.blademaker.tv/api/TIHI','https://memes.blademaker.tv/api/facepalm','https://memes.blademaker.tv/api/meme','https://memes.blademaker.tv/api/comics','https://memes.blademaker.tv/api/wholesomememes','https://memes.blademaker.tv/api/goodanimemes']
	url = random.choice(links)
	
	return url