import random
import discord
import keep_alive
import os
import time
from discord.ext import commands
import asyncio
#^ basic imports for other features of discord.py and python ^
intents = discord.Intents.none()
intents.reactions = True
intents.members = True
intents.guilds = True



client = discord.Client()

client = commands.Bot(command_prefix = 'T') #put your own prefix here

@client.event
async def on_ready():
    print("Skynet is online") #will print "bot online" in the console when the bot is online

@client.command()
async def member(ctx,member:discord.Member):
  etest = discord.Embed(
    title = "New Member: ",
    color = 0x63cf5b,
    description = "New member: " + member.mention
  )
  etest.set_thumbnail(url= member.avatar_url)
  await ctx.send(embed = etest)

#Fun
lobby = []
@client.command()
async def roulette(ctx):
    def check(msg):
        return msg.channel == ctx.channel and msg.content.lower() in ["join", "leave"]
    
    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "join":
        await ctx.send("Joining Lobby")
        lobby.append(msg.author)
    else:
        await ctx.send("Leaving Lobby.")

    await ctx.send("Roulette is now starting!  Type 'Tjoin' to join the lobby!")
  
    
#Speaking commands
@client.command()
async def back(ctx):
  await ctx.send("I'll be back.")
@client.command()
async def finish(ctx):
  await ctx.send("Hasta La Vista, Baby.")
@client.command()
async def fate(ctx):
  await ctx.send("There is not fate but what we make for ourselves.")t

#termination commands
@client.command()
@commands.has_any_role('Commisar','Oligarch','Dictator')
async def purge(ctx, num=None):
  try:
    num = int(num)
    await ctx.channel.purge(limit=num) 

  except discord.ext.commands.errors.MissingAnyRole:
    await ctx.send("No permission")

@client.command()
@commands.has_any_role('Commissar','Oligarch','Dictator')
async def terminate(ctx, member : discord.Member):
    await ctx.send("Target Acquired.")
    await ctx.send(member + " has been terminated.")
    await member.ban


@client.command()
@commands.has_any_role('Commissar','Oligarch','Dictator')
async def kick(ctx, member : discord.Member):
    await ctx.send("Terminator deployed.")
    await ctx.send(member + " has been kicked.")
    await member.kick


@client.command()
@commands.has_any_role('Commissar','Oligarch','Dictator')
async def mute(ctx, member : discord.Member):
    await ctx.send("Terminator deployed.")
    (member + " has been muted.")
    await member.mute(member + " has been muted.")


@client.command()
@commands.has_any_role('Dictator')
async def nuke(ctx, channel: discord.TextChannel):
    await ctx.send("Launching all Soviet Nukes...")
    await ctx.send("Judgement day of " + channel.name + " has arrived.")
    await channel.send("Gripping your gun, you run to the safety of the shelters.  You hear the nuclear siren wail in the distance, knowing the fate of your messages is sealed.")
    for x in range(5, 0, -1):
      await ctx.send(x)      
      time.sleep(1)
    await channel.delete()


@client.command()
@commands.has_any_role('Commissar','Oligarch','Dictator')
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel bunkered down.')


@lock.error
async def lock_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        await ctx.send('You do not have permission to use this command!') 


@client.command()
@commands.has_any_role('Commissar','Oligarch','Dictator')
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("Channel doors opening.")
    #simple command so that when you type "!ping" the bot will respond with "pong!"



keep_alive.keep_alive()
client.run(os.environ['token']) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
