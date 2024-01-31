import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("fun.py success")


    @commands.command()
    async def pfp(self, ctx, member: discord.Member):
        pfp = member.avatar.url
        await ctx.send(pfp)

    @commands.command()
    async def banner(self, ctx, member: discord.Member):
        banner = member.banner.url
        await ctx.send(banner)

    @commands.command()
    async def roll(self, ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send("Format is not dice notation.")
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(aliases=['f','coin'])
    async def flip(self, ctx):
        flip = random.randint(0,1)
        if (flip == 0):
           await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

    @commands.command(aliases=['emoji','take'])
    async def steal(ctx, emoji: discord.PartialEmoji):
        await ctx.send(emoji.url)



async def setup(client):
    await client.add_cog(Fun(client))