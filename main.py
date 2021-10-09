# main.py 
# Head function for the discord bot project

import discord
import asyncio
import json
import requests

import os
from dotenv import load_dotenv as load                                                                                                                                                                                                                                                                                          
client = discord.Client()

load()

BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
   
    # Verify that the guild the client is in is the desired guild according to the environment
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    print(
        f'{client.user} here, ready to automate. In '
        f'{guild.name}(id: {guild.id})'
    )
  
client.run(BOT_TOKEN)
