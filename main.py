import os
import discord
import requests
import json
import random
import aiohttp
import io
import time
from discord.ext import commands, tasks
from keep_alive import keep_alive
from merlin import get_merlin
from Truth_n_Dare import *
from porn_link import porn_links
from meme_nsfw_link import nsfw_links
from meme_link import meme_links
from hentai_link import hentai_links
from roll_a_die import roll_a_die_get


client = commands.Bot(command_prefix = '$')
client.remove_command("help")



#this return a respond which says is we are connected or not
@client.event
async def on_ready():
    print('bot {0.user} is online'.format(client)) 
    change_status.start()





################## HELP #####################

@client.group(invoke_without_command=True)
async def help(ctx):
	embed = discord.Embed(title="Help",description='Use `$help <description>` for extended information on that command', color=discord.Color.green())
	embed.add_field(name="Admin", value="kick, ban, Unban", inline = False)
	embed.add_field(name="General",value="dis(early-access) , clear, ping",inline = False)
	embed.add_field(name="Interactive",value="echo, Tictactoe (early-access), merlin, TnD, flp, poll", inline = False)
	embed.add_field(name="Entertainment",value="porn, meme, memes_nsfw, quotes", inline = False)
	await ctx.send(embed=embed)

### Game ###
@help.command()
async def merlin(ctx):
  embed = discord.Embed(title = "Merlin", description = "ask a yes or no question to Merlin And the great wizard will reveal to you the answer that you seek so dearly", color=discord.Color.green())
  embed.add_field(name = "**Syntax**", value = "`$merlin <Question>`")
  embed.set_thumbnail(url="http://img2.wikia.nocookie.net/__cb20130215182314/scribblenauts/images/f/fc/Wizard_Male.png")
  await ctx.send(embed = embed)

@help.command()
async def TnD(ctx):
	TnD_thumb_store=['https://www.truthordare.fr/public/img/logo.png','https://ru.lolzz.me/tord-ui/images/light-blue-red.png']
	TnD_thumb = random.choice(TnD_thumb_store)
	embed = discord.Embed(title="Truth n Dare",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$Tnd <t for truth / d for dare>`")
	embed.set_thumbnail(url=TnD_thumb)
	await ctx.send(embed=embed)

@help.command()
async def flp(ctx):
	embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$flp`")
	await ctx.send(embed=embed)

### Fun ###
@help.command()
async def memes(ctx):
	meme_thumb_store =  ['http://www.relatably.com/m/img/memes-happy-face/Happy-Face-Meme-Png-02.png','https://cdn130.picsart.com/288615163024211.png','https://i.imgflip.com/2vddr6.png']
	meme_thumb=random.choice(meme_thumb_store)
	embed = discord.Embed(title="Memes",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$memes`")
	embed.set_thumbnail(url=meme_thumb)
	await ctx.send(embed=embed)

@help.command()
async def porn(ctx):
	embed = discord.Embed(title="Porn",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$porn`")
	await ctx.send(embed=embed)

@help.command()
async def meme_nsfw(ctx):
	embed = discord.Embed(title="Meme NSFW",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$meme_nsfw`")
	await ctx.send(embed=embed)

@help.command()
async def quote(ctx):
	embed = discord.Embed(title="Quote",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$quote`")
	await ctx.send(embed=embed)

### Admin ###
@help.command()
async def echo(ctx):
	embed = discord.Embed(title="echo",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$echo <any word/emoji/link or combined>`")
	await ctx.send(embed=embed)
	
@help.command()
async def ping(ctx):
	embed = discord.Embed(title="Ping",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$ping`")
	await ctx.send(embed=embed)

@help.command()
async def clear(ctx):
	embed = discord.Embed(title="Clear",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value='`$clear [number of messages]`')
	await ctx.send(embed=embed)

@help.command()
async def dis(ctx):
	embed = discord.Embed(title="Disappearing Messages",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value='`$dis "<message>" <seconds>`')
	await ctx.send(embed=embed)

@help.command()
async def poll(ctx):
	embed = discord.Embed(title="Poll",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value='`$poll "<question>" "[option1]" "[option2]"`')
	await ctx.send(embed=embed)

@help.command()
async def tictactoe(ctx):
	embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$tictactoe <@player1> <@player2>`")
	await ctx.send(embed=embed)


@help.command()
async def kick(ctx):
	embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$kick <@member>`")
	await ctx.send(embed=embed)


@help.command()
async def ban(ctx):
	embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$ban <@member>`")
	await ctx.send(embed=embed)


@help.command()
async def unban(ctx):
	embed = discord.Embed(title="Flip a Coin",description="",color=discord.Color.green())
	embed.add_field(name="**Syntax**",value="`$unban <@member>`")
	await ctx.send(embed=embed)



################ HELP ########################


############### Commands #####################

### Ping ###

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




### Quote ###

@client.command(aliases=['q','quotes'],help='-> gives random quotes')
async def quote(ctx):
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q']
	author = '-'+json_data[0]['a']
	embed = discord.Embed(title=quote) 
	embed.set_footer(text=author) 
	await ctx.send(embed = embed)





### Merlin ###

@client.command(aliases=['merlin','mr'], help='-> Play 8ball game \n $8ball [question]')
async def Merlin(ctx,*,question = None):
	if question == None:
		await ctx.send('You forgot to ask a question \nTo know more use`$help merlin`')
	ball = get_merlin(question)
	embed = discord.Embed(description=ball,color = discord.Color.light_grey())
	embed.set_author(name = 'Merlin',icon_url = 'http://img2.wikia.nocookie.net/__cb20130215182314/scribblenauts/images/f/fc/Wizard_Male.png') 
	await ctx.send(embed=embed)



### Memes ###

@client.command(aliases=['meme','m','Meme',], help='-> gives')
async def memes(ctx,quary=None):
	if quary==None:
		url = meme_links()
		r = requests.get(url)
		res = r.json() #disc value from the website 
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
		r = requests.get(url)
		res = r.json() #disc value from the website 
		
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



### Meme_NSFW ###

@client.command(aliases=['mn','MEME_NSFW'], help='-> gives')
async def meme_nsfw(ctx):
		
		url = nsfw_links()
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



### Porn ###

@client.command(aliases=['Porn','pn'], help='-> do you really need an explanation ')
async def porn(ctx):
	url= porn_links()
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


### Hentai ###
@client.command(aliases=['ecchi','doujinshi','h','H'])
async def hentai(ctx):
	url= hentai_links()
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



### flip a coin ###

@client.command(aliases=['flip a coin','flp','coin'],help='-> flips the coin')
async def flip_a_coin(ctx):
	coin = ['Heads','Tails']
	outcome = random.choice(coin)
	embed = discord.Embed(title = f"It's a {outcome}",color = discord.Color.gold())
	if outcome == "Heads":
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/835036413907959869/837278365794304020/1619692438165.png")
	else:
		embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/835036413907959869/837278365944905768/1619692570963.png')
	embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
	await ctx.send(embed=embed)



### Truth and Dare ###

@client.command(aliases = ['t&d','truth and dare','tnd'],help = '-> play truth and date with your friends')
async def TnD(ctx,category=None):
	if category == None :
		await ctx.send('Pls chose truth(t) or False(f) \nOr use `$help TnD` to know more') 
	if category == 'truth' or category == 't':
		embed = discord.Embed(title='your truth is', description=truth())
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
	if category == 'dare' or category == 'd':
		embed = discord.Embed(title='your dare is', description=dare())
		embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)
	
### comment ###
@client.command(aliases=['comment','com'])
async def yt(ctx,*args):
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
@client.command()
async def triggered(ctx, member: discord.Member=None):
    if not member: # if no member is mentioned
        member = ctx.author # the user who ran the command will be the member
        
    async with aiohttp.ClientSession() as wastedSession:
        async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wastedImage: # get users avatar as png with 1024 size
            imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
            await wastedSession.close() # closing the session and;
            
            await ctx.reply(file=discord.File(imageData, 'triggered.gif')) # sending the file

### Echo ###

@client.command(help = "-> prompt users input")
async def echo(ctx,*args):
	await ctx.channel.purge(limit=1)
	string=''
	for words in args:
		string+=words
		string+=" "
	await ctx.send(string)



### Kick ###
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} have been kicked sucessfully")


### Ban ###

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been bannned sucessfully")


### Unban ###

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user
  
	if (user.name, user.discriminator) == (member_name, member_discriminator):
		await ctx.guild.unban(user)
		await ctx.send(f"{user} have been unbanned sucessfully")



### Disapearing Messages ###

@client.command()
async def dis(ctx,message,second='10'):
	t=int(second)
	time.sleep(t)
	await ctx.channel.purge(limit=1)



### Clear ###
@client.command()
async def clear(ctx,value='1'):
	await ctx.channel.purge(limit=1)
	limit = int(value)
	if 0 < limit <=100:
		with ctx.channel.typing():
			deleted = await ctx.channel.purge(limit=limit)

			await ctx.send(f"Deleted {len(deleted)} messages.", delete_after=5)
	else:
		await ctx.send("The limit provided is notwithin acceptable bounds")

### Kill ###
@client.command()
async def kill(ctx, friend: discord.Member):
    #bob = ctx.message.author.id

    l = ['one day <@{author}> stabed <@{friend}> to death <@{author}>']
    word = random.choice(l)
    take = word.format(author=ctx.message.author.id, friend=friend.id)
    await ctx.send(take) 

@client.command()
async def roll_a_die(ctx,value):
	die_value = str(roll_a_die_get(value))
	output = 'You get a '+die_value
	await ctx.send(output)




#### Poll ####
@client.command()
async def poll(ctx, question=None, option1=None, option2=None):
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




### TicTacToe ###

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases=['ttt','TTT'])
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command(aliases=['end_ttt',"END_TTT","endttt","ENDTTT"])
async def end(ctx):
    # We need to declare them as global first
    global count
    global player1
    global player2
    global turn
    global gameOver

    # Assign their initial value
    count = 0
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True

    # Now print your message or whatever you want
    myEmbed = discord.Embed(
        title="RESET GAME",
        description="TO START A NEW GAME, USE `$tictactoe` COMMAND",
        color=0x2ecc71)
    await ctx.send(embed=myEmbed)


################ Commands  #################

############### Status ################

@tasks.loop(seconds=60)
async def change_status():
	await client.change_presence(activity=discord.Game('Alpha testing'))

########### Status ###############

# !!!!  pls don't change the things under !!!! 
Token = os.environ['TOKEN']


keep_alive() #to run the web server 

client.run(Token)   #to run the bot