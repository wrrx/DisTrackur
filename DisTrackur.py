import discord, TOKEN, TARGETID
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime
dt = datetime.now() # defines start time

token = TOKEN.token
target = TARGETID.targetid
client=commands.Bot(command_prefix =('-'), self_bot = True) # command prefix is not needed for this script

@client.event
async def on_ready(): # script execution
    print(' ')
    print('DisTrackur : online')
    print('Started On :', dt.strftime("%H:%M:%S"))
    print('Target ID  :', target)
    print('---------------------------------------------')

@client.event
async def on_message(message): # on message
    if message.author.id == target:
        dt = datetime.now()
        time = dt.strftime("%H:%M:%S")
        print(f'{time} : {message.content}')

client.run((token), bot=False) # runs user token




# Title  : DisTrackur
# Author : 9socket
# Github : https://github.com/9socket
# Repo   : https://github.com/9socket/DisTrackur