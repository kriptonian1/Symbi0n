import discord
from discord.ext import commands
import asyncio
import typing

class Paginate:
    def __init__(self, timeout, entries, bot,index: int = 0, prefix: str ="```py\n", suffix: str ="\n```"):
        self.timeout=timeout
        self.entries = entries
        self.index = index
        self.prefix = prefix
        self.suffix = suffix
        self.embeds = []
        self.bot=bot
        self.emojis = {
            '⬅️':'prev',
            '➡️':'next' ,
            '🗑':'delete'
        }
    
    def check(self, p) -> bool:
        return p.message_id == self.message.id and p.user_id == self.author.id and p.emoji.name in self.emojis.keys()

    def create_embeds(self, author: typing.Union[discord.Member, discord.User]):

        for entry in self.entries:
            embed = discord.Embed()
            embed.description = self.prefix+entry+self.suffix
            embed.set_footer(text=author, icon_url=author.avatar_url)
            self.embeds.append(embed)
    
    async def prev(self):
        if self.index>0:
            self.index-=1
            await self.message.edit(embed=self.embeds[self.index])

    async def next(self):
        if self.index<(len(self.entries)-1):
            self.index+=1
            await self.message.edit(embed=self.embeds[self.index])

    async def delete(self):
        await self.message.delete()

        return True
    
    async def start(self, ctx: commands.Context):

        self.author = ctx.author

        self.create_embeds(ctx.author)

        self.message = await ctx.send(embed=self.embeds[self.index])

        for emoji in self.emojis.keys():
            await self.message.add_reaction(emoji)
        
        while True:
            try:
                done, pending = await asyncio.wait([self.bot.wait_for('raw_reaction_add',check=self.check),self.bot.wait_for('raw_reaction_remove',check=self.check)], return_when=asyncio.FIRST_COMPLETED, timeout=self.timeout)
                reaction = done.pop().result()

                toBreak = await getattr(self, self.emojis[reaction.emoji.name])()

                if toBreak:
                    break

            except asyncio.TimeoutError:
                self.embeds[self.index].color=0xFF0000
                await self.message.edit(embed=self.embeds[self.index])
                break