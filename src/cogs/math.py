import os
import discord
from discord.ext import commands


class math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("math.py success")
        





async def setup(client):
    await client.add_cog(math(client))