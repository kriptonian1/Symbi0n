import discord
from discord.ext import commands
import aiohttp
import json
from io import BytesIO


class Utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(aliases=['q','quotes'],help='-> gives random quotes')
	async def quote(self, ctx):
		async with aiohttp.ClientSession(loop=self.bot.loop) as session:
			response = await session.get("https://zenquotes.io/api/random")
		json_data = json.loads(await response.text())
		quote = json_data[0]['q']
		author = '-'+json_data[0]['a']
		embed = discord.Embed(title=quote) 
		embed.set_footer(text=author) 
		await ctx.send(embed = embed)
	
	@commands.command(aliases=['comment','com'])
	async def yt(self, ctx,*args):
		msg=''
		for words in args:
			msg+=words
			msg+=" "
		msg=msg.replace(' ','%20')
		user_name = ctx.author.display_name
		user_img = str(ctx.author.avatar_url)
		user_pic = user_img.replace('.webp?size=1024','.png')
		url = f"https://some-random-api.ml/canvas/youtube-comment?username={user_name}&comment={msg}&avatar={user_pic}&dark=true%E2%80%8B"
		final = url
		await ctx.send(final)
	
	#### triggered ###
	@commands.command()
	async def triggered(self, ctx, member: discord.Member=None):
		if not member: # if no member is mentioned
			member = ctx.author # the user who ran the command will be the member
			
		async with aiohttp.ClientSession(loop=self.bot.loop) as wastedSession:
			async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
				imageData = BytesIO(await wastedImage.read()) # read the image/bytes
				
				await wastedSession.close() # closing the session and;
				
				await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file
	
	@commands.command()
	async def wasted(self, ctx, member: discord.Member=None):
			if not member: # if no member is mentioned
				member = ctx.author # the user who ran the command will be the member
			
			async with aiohttp.ClientSession(loop=self.bot.loop) as wastedSession:
				async with wastedSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
					imageData = BytesIO(await wastedImage.read()) # read the image/bytes
				
				await wastedSession.close() # closing the session and;
				
				await ctx.reply(file=discord.File(imageData, 'triggered.png')) # sending the file

	@commands.command(help = "-> prompt users input")
	async def echo(self, ctx,*args):
		await ctx.channel.purge(limit=1)
		string=''
		for words in args:
			string+=words
			string+=" "
		await ctx.send(string)
	@commands.command()
	async def poll(self, ctx, question=None, option1=None, option2=None):
		if question==None:
			await ctx.send('You forgot to ask a question \nTo know more use`$help poll`')
		if option1==None and option2==None and question != None:
			await ctx.channel.purge(limit=1)
			embed = discord.Embed(title="New Poll")
			embed.add_field(name=f"**{question}**",value=f"**✅ = Yes**\n**❎ = No**")
			text = await ctx.send(embed=embed)
			await text.add_reaction('✅')
			await text.add_reaction('❎')
		elif option1==None and question != None:
			await ctx.channel.purge(limit=1)
			embed = discord.Embed(title="New Poll")
			embed.add_field(name=f"**{question}**",value=f"**✅ = {option1}**\n**❎ = No**")
			text = await ctx.send(embed=embed)
			await text.add_reaction('✅')
			await text.add_reaction('❎')
		elif option2==None and question != None:
			await ctx.channel.purge(limit=1)
			embed = discord.Embed(title="New Poll")
			embed.add_field(name=f"**{question}**",value=f"**✅ = Yes**\n**❎ = {option2}**")
			text = await ctx.send(embed=embed)
			await text.add_reaction('✅')
			await text.add_reaction('❎')
		elif question != None:
			await ctx.channel.purge(limit=1)
			embed = discord.Embed(title="New Poll")
			embed.add_field(name=f"**{question}**",value=f"**✅ = {option1}**\n**❎ = {option2}**")
			text = await ctx.send(embed=embed)
			await text.add_reaction('✅')
			await text.add_reaction('❎')

def setup(bot):
	bot.add_cog(Utils(bot))