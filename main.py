import os
import discord
import requests
import json
import random
from discord.ext import commands, tasks
from keep_alive import keep_alive
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix = '$')

def get_quote(): 
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q']+' -'+json_data[0]['a'] 
	return quote

def get_8ball(q):
	import http.client
	import json
	import urllib.parse
	conn = http.client.HTTPSConnection("8ball.delegator.com")
	question = urllib.parse.quote(q)
	conn.request('GET', '/magic/JSON/' + question)
	response = conn.getresponse()
	ans=(json.loads(response.read()))
	return (ans['magic']['answer'])




#this return a respond which says is we are connected or not
@client.event
async def on_ready():
    print('bot {0.user} is online'.format(client)) 
    change_status.start()



@client.command(aliases=['p','pings'],help='-> shows the latancy')
async def ping(ctx):
	pong = 'Pong! {0}ms'.format(round(((client.latency)*1000)))
	num_pong = round(((client.latency)*1000))
	if num_pong <= 100:
		embed = discord.Embed(description = pong,color = discord.Color.green())
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description = pong,color = discord.Color.red())
		await ctx.send(embed=embed)



@client.command(aliases=['q','quotes'],help='-> gives random quotes')
async def quote(ctx):
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q']
	author = '-'+json_data[0]['a']
	embed = discord.Embed(title=quote) 
	embed.set_footer(text=author) 
	await ctx.send(embed = embed)



@client.command(aliases=['eightball','8balls','eightballs'],name='8ball', help='-> Play 8ball game \n $8ball [question]')
async def _8ball(ctx,*,question):
	ball = get_8ball(question)
	embed = discord.Embed(description=ball,color = discord.Color.light_grey())      
	embed.set_author(name = '8ball',icon_url = 'https://www.pinclipart.com/picdir/big/524-5241376_pool-8-ball-emoji-clipart-pool-png-download.png') 
	await ctx.send(embed=embed)



@client.command(aliases=['meme','m','Meme',], help='-> gives')
async def memes(ctx):
	r = requests.get('https://memes.blademaker.tv/api?lang=en')
	res = r.json()
	title = res['title']
	ups = res['ups']
	downs = res['downs']
	sub = res['subreddit']
	m = discord.Embed(title=f"{title}\nsubreddit: {sub}",color=discord.Color.blue())   
	m.set_image(url = res["image"])
	m.set_footer(text=f"👍:{ups}   👎:{downs}") 
	await ctx.send(embed=m)

@client.command(aliases=['mn','MEME_NSFW'], help='-> gives')
async def meme_nsfw(ctx):
		r = requests.get('https://memes.blademaker.tv/api/nswf')
		res = r.json()
		title = res['title']
		ups = res['ups']
		downs = res['downs']
		sub = res['subreddit']
		m = discord.Embed(title=f"{title}\nsubreddit: {sub}",color=discord.Color.red())
		m.set_image(url = res["image"])
		m.set_footer(text=f"👍:{ups}   👎:{downs}") 
		await ctx.send(embed=m)

@client.command(aliases=['Porn','pn','PORN'], help='-> do you really need an explanation ')
async def porn(ctx):
	links=['https://memes.blademaker.tv/api/onlyfansgirls101','https://memes.blademaker.tv/api/Nudes','https://memes.blademaker.tv/api/boysgonewild']
	url=random.choice(links)
	r = requests.get(url)
	res = r.json()
	title = res['title']
	ups = res['ups']
	downs = res['downs']
	sub = res['subreddit']
	m = discord.Embed(title=f"{title}\nsubreddit: {sub}",color=discord.Color.dark_magenta())
	m.set_image(url = res["image"])
	m.set_footer(text=f"👍:{ups}   👎:{downs}") 
	await ctx.send(embed=m)

@tasks.loop(seconds=60)
async def change_status():
	await client.change_presence(activity=discord.Game('Pre alpha testing'))



# pls don't change the things under 
Token = os.environ['TOKEN']



keep_alive() #to run the web server 
client.run(Token) 