import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import youtube_dl
#import fortnite_api
import random
from gpt4all import GPT4All
from openai import OpenAI
import cogs.music as music

cogs = [music]


load_dotenv()

token = os.getenv('token')

oaitoken = os.getenv('oaitoken')

system_prompt = os.getenv('system_prompt')

intents = discord.Intents.all()

client = commands.Bot(command_prefix=";", intents = intents)
ClientAi = OpenAI(api_key=oaitoken)

async def load():
     for filename in os.listdir("./src/cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename[:-3]}")


# GPT4All Support
## model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf", device='gpu')
## system_template = ""

@client.event
async def on_ready():
    print(f"Success: {client.user} Online.")


@client.command(aliases=["ping", 'ms'])
async def hey(ctx):
    await ctx.send("Haii! Latency: {0}ms!" .format(round(client.latency * 1000)))

# Requires Access to a Fortnite API
## @client.command()
## async def fnshop(ctx):
##     # shoprequest = 
##     embed = discord.Embed(title="Daily Fn Shop!")
##     embed.set_image(url=data[""])
##     await ctx.send(embed = embed)
    
async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())