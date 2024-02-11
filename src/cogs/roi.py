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
    async def afk(self, ctx):
        async with ctx.typing():
            count = open('./src/afk.txt', 'r')
            number = int(count.read())
            count.close
            writenumber = open('./src/afk.txt', 'w')
            number = number+1
            number1 = writenumber.write(str(number))
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
            await ctx.send(f'roi went afk for the {ordinal(number)} time')
            writenumber.close



async def setup(client):
    await client.add_cog(roi(client))
