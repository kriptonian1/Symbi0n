import discord
from discord.ext import commands
from utils import Utils
import requests
import aiohttp
from io import BytesIO

class NSFW(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.utils = Utils()
	
	async def cog_check(self, ctx):
		await ctx.send('You need to run this command in a nsfw channel')
		return ctx.channel.is_nsfw()
	
	@commands.command(aliases=['mn','memes_nsfw','memes nsfw','meme nsfw','memes n','meme n','memes_n','meme_n'], help='-> gives')
	async def meme_nsfw(self, ctx):
			
			url = self.utils.get_nsfw_link()
			r = requests.get(url)
			res = r.json()
			title = res['title']
			ups = res['ups']
			Id = res['id']
			downs = res['downs']
			sub = res['subreddit']
			title_link = title.replace(" ","_")
			reddit_link = "https://www.reddit.com/r/"+sub+"/comments/"+Id+"/"+title_link+"/"
			m = discord.Embed(title=f"{title}\nsubreddit: {sub}",url=reddit_link,color=discord.Color.red())
			m.set_image(url = res["image"])
			m.set_footer(text=f"👍:{ups}   👎:{downs}") 
			await ctx.send(embed=m)
		
	@commands.command(aliases=['pn'], help='-> do you really need an explanation ')
	async def porn(self, ctx):
		url= self.utils.get_porn_link()
		r = requests.get(url)
		res = r.json()
		title = res['title']
		ups = res['ups']
		downs = res['downs']
		Id = res['id']
		sub = res['subreddit']
		title_link = title.replace(" ","_")
		reddit_link = "https://www.reddit.com/r/"+sub+"/comments/"+Id+"/"+title_link+"/"
		m = discord.Embed(title=f"{title}\nsubreddit: {sub}",url=reddit_link,color=discord.Color.dark_magenta())
		m.set_image(url = res["image"])
		m.set_footer(text=f"👍:{ups}   👎:{downs}") 
		await ctx.send(embed=m)
	
	@commands.command(aliases=['ecchi','doujinshi','h'])
	async def hentai(self, ctx):
		url= self.utils.get_hentai_link()
		r = requests.get(url)
		res = r.json()
		title = res['title']
		ups = res['ups']
		downs = res['downs']
		Id = res['id']
		sub = res['subreddit']
		title_link = title.replace(" ","_")
		reddit_link = "https://www.reddit.com/r/"+sub+"/comments/"+Id+"/"+title_link+"/"
		m = discord.Embed(title=f"{title}\nsubreddit: {sub}",url=reddit_link,color=discord.Color.dark_magenta())
		m.set_image(url = res["image"])
		m.set_footer(text=f"👍:{ups}   👎:{downs}") 
		await ctx.send(embed=m)
	
	@commands.command()
	async def horny(self, ctx, member: discord.Member=None):
			if not member: # if no member is mentioned
				member = ctx.author # the user who ran the command will be the member
			
			async with aiohttp.ClientSession(loop=self.bot.loop) as wastedSession:
				async with wastedSession.get(f'https://some-random-api.ml/canvas/horny?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
					imageData = BytesIO(await wastedImage.read()) # read the image/bytes
				
				await wastedSession.close() # closing the session and;
				
				await ctx.reply(file=discord.File(imageData, 'horny.png')) # sending the file

def setup(bot):
	bot.add_cog(NSFW(bot))