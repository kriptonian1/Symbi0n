import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        await ctx.send(f"{user} have been kicked sucessfully")


    ### Ban ###

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        await ctx.send(f"{user} have been bannned sucessfully")


    ### Unban ###

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
    
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user} have been unbanned sucessfully")
    
    @commands.command()
    async def clear(sef, ctx, value='1'):
        await ctx.channel.purge(limit=1)
        limit = int(value)
        if 0 < limit <=100:
            with ctx.channel.typing():
                deleted = await ctx.channel.purge(limit=limit)

                await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
        else:
            await ctx.send("The limit provided is notwithin acceptable bounds")

def setup(bot):
    bot.add_cog(Moderation(bot))