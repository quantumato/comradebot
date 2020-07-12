# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!\n')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel_send(
        f'Hi {member.name}, welcome to our little shitfest'
        )

client.run(TOKEN)
