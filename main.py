
import discord
import keep_alive
import os
import time
from discord.ext import commands
#^ basic imports for other features of discord.py and python ^

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

#Speaking commands
@client.command()
async def back(ctx):
  await ctx.send("I'll be back.")
@client.command()
async def finish(ctx):
  await ctx.send("Hasta La Vista, Baby.")
@client.command()
async def fate(ctx):
  await ctx.send("There is not fate but what we make for ourselves.")

#calculations
@client.command()
async def calculate(ctx, num1, num2):
  #Store number variables for the two numbers

#the sum of the two numbers variable
  sum = float(num1) + float(num2)
  sum2 = float(num1) - float(num2)
  sum3 = float(num1) * float(num2)
  sum4 = float(num1) / float(num2)

#what operator to use
  choice = input('Enter an operator, + = addition, - = subtraction, * = multiplication and / = division: ')
#different sums based on the operators
  if choice == '+':
    await ctx.send('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

  if choice == '-':
    await ctx.send('The sum of {0} and {1} is {2}'.format(num1, num2, sum2))

  if choice == '*':
    await ctx.send('The sum of {0} and {1} is {2}'.format(num1, num2, sum3))

  if choice == '/':
    await ctx.send('The sum of {0} and {1} is {2}'.format(num1, num2, sum4))

#termination commands
@client.command()
async def purge(ctx, message,num = None):
    if not num:
      for x in range(num):
        message.delete()
    else:
      try:
        message.delete()
      except:
        await ctx.send("No targets to terminate.")
        

    await ctx.send("Terminator deployed.")
    await message.delete()
@client.command()
async def terminate(ctx, member : discord.Member):
    await ctx.send("Target Acquired.")
    await ctx.send(member + " has been terminated.")
    await member.ban
@client.command()
async def kick(ctx, member : discord.Member):
    await ctx.send("Terminator deployed.")
    await ctx.send(member + " has been kicked.")
    await member.kick
@client.command()
async def mute(ctx, member : discord.Member):
    await ctx.send("Terminator deployed.")
    (member + " has been muted.")
    await member.mute(member + " has been muted.")
@client.command()
async def nuke(ctx, channel):
    await ctx.send("Launching all Soviet Nukes...")
    await ctx.send("Judgement day of " + channel + " has arrived.")
    for x in range(5, 0, -1):
      await ctx.send(x)
      time.sleep(1)
    await ctx.channel.delete()
@client.command()
@commands.has_permissions(manage_channels=True)
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
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("Channel doors opening.")
    #simple command so that when you type "!ping" the bot will respond with "pong!"

#Test
keep_alive.keep_alive()
client.run(os.environ['token']) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
