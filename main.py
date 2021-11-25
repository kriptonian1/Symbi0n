import os
import io
import textwrap
import traceback
import contextlib
import discord

from decouple import config

from discord.ext import commands
from discord.flags import Intents

from botutils.general import CallFromList, call, print_error
from botutils.common import Paginate

CFL = CallFromList()

class Symbion(commands.Bot):

    def __init__(self, **kwargs):
        
        self.token = kwargs.pop('token', None)
        self.prefix = kwargs.pop('prefix', "$") # TODO: Change it to read from DB later

        super().__init__(
                        command_prefix=self.prefix,
                        activity=discord.Game(name="Alpha testing"), 
                        **kwargs
                    )

    async def start_CFL(self):
        """This is called on bot startup"""

        await CFL.call(self)

    # Adds command to the list of commands
    def add_command(self, command: commands.Command):
        super().add_command(command)

        # 2 SEC NEEDED TO RUN A COMMAND
        command.cooldown_after_parsing = True
        if not getattr(command._buckets, "_cooldown", None):
            command._buckets = commands.CooldownMapping.from_cooldown(1, 2, commands.BucketType.user)
    
    # Custom Command Invoker
    async def invoke(self, ctx: commands.Context, **flags):
        dispatch = flags.pop("dispatch", True)

        if ctx.command is not None:
            if dispatch:
                self.dispatch("command", ctx)
            
            try:
                check = await self.can_run(ctx, call_once=flags.pop("call_once", True))

                if check or not flags.pop("call_check", True):
                    await ctx.command.invoke(ctx)
                else:
                    raise commands.CheckFailure("Check Once Failure")

            except commands.CommandError as err:
                if dispatch:
                    await ctx.command.dispatch_error(ctx, err)
                if flags.pop("redirect_error", False):
                    raise

            else:
                if dispatch:
                    self.dispatch("command_completion", ctx)
        
        elif ctx.invoked_with:
            err = commands.CommandNotFound(f'Command "{ctx.invoked_with}" was not found.')

            if dispatch:
                self.dispatch("command_error", ctx, err)
            
            if flags.pop("redirect_error", False):
                raise err


    @property
    def bot_owners_list(self):
        return [self.get_user(x) for x in self.owner_ids]
    
    async def on_ready(self):
        print(f"{self.user} is ready to operate.")

    async def on_connect(self):
        print(f"{self.user} connected!")

    async def on_disconnect(self):
        print(f"{self.user} disconnected.")


    @CFL.append
    def load_cogs(self):
        """Load bot extensions/cogs from cogs subdirectory"""

        print("Loading Cog")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                cog_name = filename[:-3]
                if err := call(self.load_extension, f"cogs.{cog_name}", ret=True):
                    print_error(f"Exception while loading extension: {cog_name}", err)
                else:
                    print(f"Loaded Cog: {cog_name}")
    

    def get_message(self, msg_id: int):
        """Retrieves a message from cache"""

        return self._connection._get_message(msg_id)
    

    async def process_commands(self, message: discord.Message):
        """Use invoke over the default process_commands"""

        if message.author.bot:
            return
        
        ctx = await self.get_context(message)
        await self.invoke(ctx)
    

    def start_bot(self):
        """ CONNECT TO WEBSOCKET AND LOAD COGS """

        self.loop.run_until_complete(self.start_CFL())
        self.run(self.token)

# CONFIGURE INTENTS
intents = Intents.default()
intents.members = True

# INSTANTIATE BOT
bot_args = {
    "owner_ids": [448359781095440385, 707876147324518440],
    "intents": intents,
    "help_command": None,
    "case_insensitive": True,
    "token": config("TOKEN")
}
bot = Symbion(**bot_args)


# LOAD A NEW COG
@bot.command(
    name="load",
    help="Load a cog into the bot.",
    hidden=True
)
@commands.is_owner()
async def load(ctx, extension):
    msg = await ctx.send("Loading {}...".format(extension))
    try:
        bot.load_extension(f'cogs.{extension}')
        await msg.edit(content=f"Loaded {extension}")
    except ImportError:
        await msg.edit(content=f"Failed to load {extension}.")


# UNLOAD A LOADED COG
@bot.command(
    name="unload",
    help="Unload a cog from the bot.",
    hidden=True
)
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded {extension}")
    except:
        await ctx.send(f"No extension of name {extension} is loaded.")


# RELOAD A COG WITH NEW CHANGES
@bot.command(
    name="reload",
    help="Reload/Refresh a loaded a cog.",
    hidden=True
)
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f"Reloaded {extension}")
    except:
        await ctx.send(f"No extension of name {extension} is loaded.")

@bot.command(aliases=['p','pings'],help='-> shows the latancy')
async def ping(ctx):
	pong = '🏓 Pong! {0}ms'.format(round(((bot.latency)*1000)))
	num_pong = round(((bot.latency)*1000))
	if num_pong <= 100:
		embed = discord.Embed(description = pong,color = discord.Color.green())
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description = pong,color = discord.Color.red())
		await ctx.send(embed=embed)

def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])
    else:
        return content

@bot.command(
    name="eval",
    help="A God command for gods",
    hidden=True
)
@commands.is_owner()
async def eval(ctx, *, code: str):
    code = cleanup_code(code)

    local_variables = {
		"discord": discord,
		"commands": commands,
		"bot": bot,
		"ctx": ctx,
		"channel": ctx.channel,
		"author": ctx.author,
		"guild": ctx.guild,
		"message": ctx.message
	}

    stdout = io.StringIO()

    try:
	    with contextlib.redirect_stdout(stdout):
		    exec(
				f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
			)

		    obj = await local_variables["func"]()
		    result = f"{stdout.getvalue()}\n-- {obj}\n"
    except Exception as e:
	    result = "".join(traceback.format_exception(e, e, e.__traceback__))

    pager = Paginate(
		timeout=100,
		entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
		index=0,
		prefix="```py\n",
		suffix="\n```",
        bot=bot
	)

    await pager.start(ctx)


bot.start_bot()