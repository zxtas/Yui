import discord
from discord.ext import commands
import random
import requests
import os
import json
xrapidapi = os.getenv('xrapidapi')

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("fun.py success")


    @commands.command()
    async def pfp(self, ctx, member: discord.Member):
        async with ctx.typing():
            pfp = member.avatar.url
            await ctx.send(pfp)

    @commands.command()
    async def banner(self, ctx, member: discord.Member):
        async with ctx.typing():
            banner = member.banner.url
            await ctx.send(banner)

    @commands.command()
    async def roll(self, ctx, dice: str):
        async with ctx.typing():
            try:
                rolls, limit = map(int, dice.split('d'))
            except Exception:
                await ctx.send("Format is not dice notation.")
                return

            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await ctx.send(result)

    @commands.command(aliases=['f','coin'])
    async def flip(self, ctx):
        async with ctx.typing():
            flip = random.randint(0,1)
            if (flip == 0):
               await ctx.send("Heads!")
            else:
                await ctx.send("Tails!")

    @commands.command(aliases=['emoji','take'])
    async def steal(self, ctx, emoji: discord.PartialEmoji):
        async with ctx.typing():
            await ctx.send(emoji.url)

    @commands.command()
    async def wyr(self, ctx):
        async with ctx.typing():
            url = "https://would-you-rather.p.rapidapi.com/wyr/random"
        headers = {
                	"X-RapidAPI-Key": f"{xrapidapi}",
                	"X-RapidAPI-Host": "would-you-rather.p.rapidapi.com"
                }
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        for findquestion in response_json:
            await ctx.send(findquestion['question'])



            





async def setup(client):
    await client.add_cog(Fun(client))