import discord, TOKEN, TARGETID
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

dt = datetime.now()

token = TOKEN.token
target = TARGETID.targetid
client=commands.Bot(command_prefix =('-'), self_bot = True)

@client.event
async def on_ready():
    print(' ')
    print('DisTrackur : online')
    print('Started On :', dt.strftime("%H:%M:%S"))
    print('Target ID  :', target)

@client.event
async def on_message(message):
    if message.author.id == target:
        dt = datetime.now()
        time = dt.strftime("%H:%M:%S")
        print(f'{time} : {message.content}')

client.run((token), bot=False)