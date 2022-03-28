import discord
from discord.ext import commands
import os
import keep_alive

#discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
client = commands.Bot(command_prefix="!",status=discord.Status.idle,activity=discord.Game(name="花兩小時建的環境"))



@client.event
async def on_ready():
    print(' >> discord bot: {0.user} is online. << '.format(client))
    
    
# 下兩行順序不可交換
keep_alive.keep_alive()   
client.run(os.getenv('token'))
