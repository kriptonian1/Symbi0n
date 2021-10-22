import discord
from discord.ext import commands
from utils import Utils
import aiohttp
import random
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.utils = Utils()
    
    @commands.command(aliases=['mr'], help='-> Play 8ball game \n $8ball [question]')
    async def Merlin(self, ctx,*,question = None):
        if question == None:
            await ctx.send('You forgot to ask a question \nTo know more use`$help merlin`')
        ball = self.utils.get_merlin(question)
        embed = discord.Embed(description=ball,color = discord.Color.light_grey())
        embed.set_author(name = 'Merlin',icon_url = 'http://img2.wikia.nocookie.net/__cb20130215182314/scribblenauts/images/f/fc/Wizard_Male.png') 
        await ctx.reply(embed=embed)
    
    @commands.command(aliases=['meme','m'], help='-> gives')
    async def memes(self, ctx,quary=None):
        if quary==None:
            url = self.utils.get_meme_link()
            async with aiohttp.ClientSession(loop=self.bot.loop) as session:
                r = await session.get(url)
            res = await r.json() #disc value from the website 
            title = res['title']
            ups = res['ups']
            downs = res['downs']
            sub = res['subreddit']
            Id = res['id']
            title_link = title.replace(" ","_")
            reddit_link = "https://www.reddit.com/r/"+sub+"/comments/"+Id+"/"+title_link+"/"
            embed = discord.Embed(title=f"{title}\nsubreddit: {sub}",url=reddit_link,color=discord.Color.blue())   
            embed.set_image(url = res["image"])
            embed.set_footer(text=f"👍:{ups}   👎:{downs}") 

            await ctx.send(embed=embed)
        else:
            url = "https://memes.blademaker.tv/api/{}".format(quary)
            async with aiohttp.ClientSession(loop=self.bot.loop) as session:
                r = await session.get(url)
            res = await r.json() #disc value from the website 
            
            try:
                title = res['title']
                ups = res['ups']
                downs = res['downs']
                sub = res['subreddit']
                Id = res['id']
                title_link = title.replace(" ","_")
                reddit_link = "https://www.reddit.com/r/"+sub+"/comments/"+Id+"/"+title_link+"/"
                embed = discord.Embed(title=f"{title}\nsubreddit: {sub}",url=reddit_link,color=discord.Color.blue())   
                embed.set_image(url = res["image"])
                embed.set_footer(text=f"👍:{ups}   👎:{downs}") 
                await ctx.send(embed=embed)

            except KeyError:
                await ctx.send('subreddit not found')
        
    @commands.command(aliases=['flip a coin','flp','coin'],help='-> flips the coin')
    async def flip_a_coin(self, ctx):
        coin = ['Heads','Tails']
        outcome = random.choice(coin)
        embed = discord.Embed(title = f"It's a {outcome}",color = discord.Color.gold())
        if outcome == "Heads":
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/835036413907959869/837278365794304020/1619692438165.png")
        else:
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/835036413907959869/837278365944905768/1619692570963.png')
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    
    @commands.command(aliases = ['t&d','truth and dare'],help = '-> play truth and date with your friends')
    async def TnD(self, ctx, category=None):
        if category == None :
            await ctx.send('Pls chose truth(t) or False(f) \nOr use `$help TnD` to know more') 
        if category == 'truth' or category == 't':
            embed = discord.Embed(title='your truth is', description=self.utils.get_truth_question())
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if category == 'dare' or category == 'd':
            embed = discord.Embed(title='your dare is', description=self.utils.get_dare_question())
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command()
    async def kill(self, ctx, friend: discord.Member):
        #bob = ctx.message.author.id

        l = ['one day <@{author}> stabed <@{friend}> to death <@{author}>']
        word = random.choice(l)
        take = word.format(author=ctx.message.author.id, friend=friend.id)
        await ctx.send(take) 

    @commands.command()
    async def roll_a_die(self, ctx,value):
        die_value = str(self.utils.get_die(value))
        output = 'You get a '+die_value
        await ctx.send(output)
    
    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None,price = None):
        if user == None:
            user = ctx.author
        
        wanted = Image.open("wanted.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((321,321))
        wanted.paste(pfp,(123,250))

        wanted.save("profile.jpg")

        img = Image.open("profile.jpg")
        font = ImageFont.truetype("Go_2_Old_Western.ttf",64)

        draw = ImageDraw.Draw(img)

        price_val = ['1000','200','177013','404','420','80085','69','696969','5318008','42','101','300','316','419','9000','911','666','999','777'] 
        if price == None:
            price = random.choice(price_val)

        draw.text((220,620),price,(0,0,0),font=font,align = "center")

        img.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))


def setup(bot):
    bot.add_cog(Game(bot))