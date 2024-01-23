import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')

intents = discord.Intents.All()

client = commands.Bot(command_Prefix=";", intents = intents)

@client.event
async def ready():
    print(f"Success: {client.user} Online.")



