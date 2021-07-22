import discord
from discord.ext import commands

#import token
# from apikeys import *
intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix = '!', intents=intents)


@client.event
async def on_ready():
    print("The bot is now ready to use")
    print("---------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("สวัสดีค่าาาาาา") 

@client.command()
async def cmds(ctx):
    await ctx.send("-----") 

@client.event
async def on_member_join(member):
    channel = client.get_channel('channel-id')
    await channel.send("Helo")

@client.event
async def on_member_remove(member):
    channel = client.get_channel('channel-id')
    await channel.send("Bye")

# place temporary token in here just for testing 
client.run('token here')
