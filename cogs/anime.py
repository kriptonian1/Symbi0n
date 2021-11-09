import discord
from discord.ext import commands
import json
import aiohttp

class Anime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['aq','anime_quote'])
    async def quote_anime(self, ctx):
        async with aiohttp.ClientSession(loop=self.bot.loop) as session:
            response = await session.get("https://some-random-api.ml/animu/quote")
        json_data = json.loads(await response.text())
        quote = json_data["sentence"]
        characther = json_data["characther"]
        anime = json_data["anime"]
        embed = discord.Embed(title=quote)
        embed.set_footer(text=characther+f"({anime})")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Anime(bot))