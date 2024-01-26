import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import asyncio
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

@client.command()
async def fnshop(ctx):
    shop = fortapi.shop.fetch()
    ctx.send(shop)

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
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Format is not dice notation.")
        return
    
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


async def main():
    async with client:
       # await load()
        await client.start(token)

asyncio.run(main())