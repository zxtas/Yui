import os
import discord
from discord.ext import commands
import ast
asttest = ast.literal_eval(str(2+2))
print(f'{asttest}', 'tested')


class math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("math.py success")

    @commands.command()
    async def eval(self, ctx, *, expression: str):
        async with ctx.typing():
            try:
                answer = numexpr.evaluate(expression)

                await ctx.send(f"{answer}")
            except:
                await ctx.send("Invalid expression.")



async def setup(client):
    await client.add_cog(math(client))
