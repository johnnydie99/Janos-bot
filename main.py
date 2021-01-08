import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive  

client = commands.Bot(command_prefix='j')

status = cycle(['Il Conoscitore Italiano','La vostra conversazione👀'])

@client.event
async def on_ready():
    change_status.start()
    print('Loggato come {0.user}'.format(client))

@tasks.loop(seconds=60)
async def change_status():
 await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=(next(status))))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()  
client.run(os.getenv('TOKEN'))  
