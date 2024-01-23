import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio

load_dotenv()

token = os.getenv('token')

intents = discord.Intents.all()

client = commands.Bot(command_prefix=";", intents = intents)

@client.event
async def on_ready():
    print(f"Success: {client.user} Online.")

@client.command(aliases=['emoji','take'])
async def steal(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)

@client.command
async def upload(ctx, fil)

@client.command(aliases=["ping", 'ms'])
async def hey(ctx):
    await ctx.send("{0}ms." .format(round(client.latency * 1000)))

async def main():
    async with client:
       # await load()
        await client.start(token)

asyncio.run(main())