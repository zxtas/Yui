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


load_dotenv()

token = os.getenv('token')

oaitoken = os.getenv('oaitoken')

system_prompt = os.getenv('system_prompt')

intents = discord.Intents.all()

client = commands.Bot(command_prefix=";", intents = intents)
ClientAi = OpenAI(api_key=oaitoken)

# GPT4All Support
## model = GPT4All("gpt4all-falcon-newbpe-q4_0.gguf", device='gpu')
## system_template = ""

@client.event
async def on_ready():
    print(f"Success: {client.user} Online.")

@client.command(aliases=['emoji','take'])
async def steal(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)

@client.command(aliases=["ping", 'ms'])
async def hey(ctx):
    await ctx.send("{0}ms." .format(round(client.latency * 1000)))

# Requires Access to a Fortnite API
## @client.command()
## async def fnshop(ctx):
##     # shoprequest = 
##     embed = discord.Embed(title="Daily Fn Shop!")
##     embed.set_image(url=data[""])
##     await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = None):
    if reason == None:
        reason == "No Reason Provided."
    message = f"You have been banned from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason = reason)
    await ctx.channel.send(f'{ctx.message.author.mention} has Banned {member.mention} for {reason}')

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    if reason == None:
        reason == "No Reason Provided."
    message = f"You have been kicked from {ctx.guild.name} for {reason}"
    await member.send(message)
    await ctx.guild.kick(member, reason = reason)
    await ctx.channel.send(f'{ctx.message.author.mention} has kicked {member.mention} for {reason}')

@client.command()
async def pfp(ctx, member: discord.Member):
    pfp = member.avatar.url
    await ctx.send(pfp)

@client.command()
async def banner(ctx, member: discord.Member):
    banner = member.banner.url
    await ctx.send(banner)

@client.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Format is not dice notation.")
        return
    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@client.command(aliases=['f','coin'])
async def flip(ctx):
    flip = random.randint(0,1)
    if (flip == 0):
       await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")


@client.command(aliases=['r','ai'])
async def request(ctx, *, question):
    question1 = str(question)
    response = ClientAi.chat.completions.create(
        model = 'gpt-4',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user","content": question1 }
        ]
    )
    print(response)
    await ctx.send(response.choices[0].message.content)
    

@client.command()
async def img(ctx, *, prompt):
    prompt1 = str(prompt)
    generated_image = ClientAi.images.generate(
        model = 'dall-e-3',
        prompt = f"I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: {prompt1}",
        size = "1792x1024",
        quality="hd",
        n=1,  
    )
    print(generated_image)
    image_url = generated_image.data[0].url
    await ctx.send(image_url)

@client.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, count):
         await ctx.channel.purge(limit = int(count) + 1)
         await ctx.send(f"Purged {count} messages!")

@client.command()
async def leave(ctx):
    voice_client = ctx.message.guid.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("Not connected to a voice channel.")


async def main():
    async with client:
       # await load()
        await client.start(token)

asyncio.run(main())