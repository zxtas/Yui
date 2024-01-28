import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
import youtube_dl
#import fortnite_api
import random


load_dotenv()

token = os.getenv('token')

intents = discord.Intents.all()

client = commands.Bot(command_prefix=";", intents = intents)

#fortapi = fortnite_api.FortniteAPI()

@client.event
async def on_ready():
    print(f"Success: {client.user} Online.")

@client.command(aliases=['emoji','take'])
async def steal(ctx, emoji: discord.PartialEmoji):
    await ctx.send(emoji.url)

@client.command(aliases=["ping", 'ms'])
async def hey(ctx):
    await ctx.send("{0}ms." .format(round(client.latency * 1000)))

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

@client.command()
async def flip(ctx):
    flip = random.randint(0,1)
    if (flip == 0):
       await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")


@client.command()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel.")
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()


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