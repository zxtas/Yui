import os
import discord
from discord.ext import commands
import random
print(os.listdir('./src'))
class roi(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("roi.py success")


    @commands.command(aliases=['bruh','crash'])
    async def crashed(self, ctx):
        async with ctx.typing():
            count = open('./src/afk.txt', 'r')
            number = int(count.read())
            count.close
            writenumber = open('./src/afk.txt', 'w')
            number = number+1
            number1 = writenumber.write(str(number))
            await ctx.send('Looks like roi crashed again!')
            await ctx.send(f'Crash Counter: {number}!')
            writenumber.close



async def setup(client):
    await client.add_cog(roi(client))
