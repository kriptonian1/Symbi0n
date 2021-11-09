import discord
from discord.ext import commands
import random

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title="Help",description='Use `$help <description>` for extended information on that command', color=discord.Color.green())
        embed.add_field(name="Admin", value="kick, ban, Unban", inline = False)
        embed.add_field(name="General",value="dis(early-access) , clear, ping",inline = False)
        embed.add_field(name="Interactive",value="echo, Tictactoe (early-access), merlin, TnD, flp, poll, horny,yt, wasted, triggered", inline = False)
        embed.add_field(name="Entertainment",value="porn, meme, memes_nsfw, quotes, anime_quote", inline = False)
        await ctx.send(embed=embed)

    ### Game ###
    @help.command()
    async def merlin(self, ctx):
        embed = discord.Embed(title = "Merlin", description = "ask a yes or no question to Merlin And the great wizard will reveal to you the answer that you seek so dearly", color=discord.Color.green())
        embed.add_field(name = "**Syntax**", value = "`$merlin <Question>`")
        embed.set_thumbnail(url="http://img2.wikia.nocookie.net/__cb20130215182314/scribblenauts/images/f/fc/Wizard_Male.png")
        await ctx.send(embed = embed)

    @help.command()
    async def TnD(self, ctx):
        TnD_thumb_store=['https://www.truthordare.fr/public/img/logo.png','https://ru.lolzz.me/tord-ui/images/light-blue-red.png']
        TnD_thumb = random.choice(TnD_thumb_store)
        embed = discord.Embed(title="Truth n Dare",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$Tnd <t for truth / d for dare>`")
        embed.set_thumbnail(url=TnD_thumb)
        await ctx.send(embed=embed)

    @help.command()
    async def flp(self, ctx):
        embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$flp`")
        await ctx.send(embed=embed)

    ### Fun ###
    @help.command()
    async def memes(self, ctx):
        meme_thumb_store =  ['http://www.relatably.com/m/img/memes-happy-face/Happy-Face-Meme-Png-02.png','https://cdn130.picsart.com/288615163024211.png','https://i.imgflip.com/2vddr6.png']
        meme_thumb=random.choice(meme_thumb_store)
        embed = discord.Embed(title="Memes",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$memes`")
        embed.set_thumbnail(url=meme_thumb)
        await ctx.send(embed=embed)

    @help.command()
    async def porn(self, ctx):
        embed = discord.Embed(title="Porn",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$porn`")
        await ctx.send(embed=embed)

    @help.command()
    async def memes_nsfw(self, ctx):
        embed = discord.Embed(title="Meme NSFW",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$memes_nsfw`")
        await ctx.send(embed=embed)

    @help.command()
    async def quote(self, ctx):
        embed = discord.Embed(title="Quote",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$quote`")
        await ctx.send(embed=embed)

    ### Admin ###
    @help.command()
    async def echo(self, ctx):
        embed = discord.Embed(title="echo",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$echo <any word/emoji/link or combined>`")
        await ctx.send(embed=embed)
        
    @help.command()
    async def ping(self, ctx):
        embed = discord.Embed(title="Ping",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$ping`")
        await ctx.send(embed=embed)

    @help.command()
    async def clear(self, ctx):
        embed = discord.Embed(title="Clear",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value='`$clear [number of messages]`')
        await ctx.send(embed=embed)

    @help.command()
    async def dis(self, ctx):
        embed = discord.Embed(title="Disappearing Messages",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value='`$dis "<message>" <seconds>`')
        await ctx.send(embed=embed)

    @help.command()
    async def poll(self, ctx):
        embed = discord.Embed(title="Poll",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value='`$poll "<question>" "[option1]" "[option2]"`')
        await ctx.send(embed=embed)

    @help.command()
    async def tictactoe(self, ctx):
        embed = discord.Embed(title="TicTacToe",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$tictactoe <@player1> <@player2>`\n`$place <box number>`")
        await ctx.send(embed=embed)


    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$kick <@member>`")
        await ctx.send(embed=embed)


    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$ban <@member>`")
        await ctx.send(embed=embed)


    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
        embed.add_field(name="**Syntax**",value="`$unban <@member>`")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))