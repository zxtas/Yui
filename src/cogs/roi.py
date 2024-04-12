import os
import discord
from discord.ext import commands
import random
<<<<<<< HEAD
print(os.listdir('/home/container/Blair/src'))
=======
from datetime import datetime, timedelta
print(os.listdir('./src'))
>>>>>>> f22d5e0e78c5ca3c60aaf389f3d6e8a28e2b859b
class roi(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("roi.py success")


    @commands.command(aliases=['bruh','crash'])
    async def afk(self, ctx):
        async with ctx.typing():
            count = open('/home/container/Blair/src/afk.txt', 'r')
            number = int(count.read())
            count.close
            writenumber = open('/home/container/Blair/src/afk.txt', 'w')
            number = number+1
            number1 = writenumber.write(str(number))
            roiinfo = os.stat('./src/afk.txt')
            lastafk = timedelta(milliseconds=roiinfo.st_mtime)
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
            await ctx.send(f'<@275459983888613376> went afk for the {ordinal(number)} time, Last Afk {lastafk}')
            writenumber.close



async def setup(client):
    await client.add_cog(roi(client))
