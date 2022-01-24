import discord
from discord.ext import commands
import os

#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
client = commands.Bot(command_prefix="!",status=discord.Status.idle,activity=discord.Game(name="花兩小時建的環境"))



@client.event
async def on_ready():
    print(' >> discord bot: {0.user} is online. << '.format(client))
    
    
    
    
client.run(os.getenv('token'))
