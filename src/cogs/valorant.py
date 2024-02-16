import os
import discord
from discord.ext import commands


class val(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("val.py success")







async def setup(client):
    await client.add_cog(val(client))