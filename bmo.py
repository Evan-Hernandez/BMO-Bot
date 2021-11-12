#bmo.py
import os

#libraries
import discord
from dotenv import load_dotenv

#loads token and other info
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

#client=bot
client = discord.Client()

@client.event
async def on_ready(): #on startup
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to Discord!\n'
        f'{client.user} is connect to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
        )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members :\n - {members}')

##async def




client.run(TOKEN)