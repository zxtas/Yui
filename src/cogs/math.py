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
        
#    @commands.Cog.listener()
#    async def on_message(self, message):
#        if message.author == self.client.user:
#            return
#        print(ast.literal_eval(f"{message.content}"))
        

        


        #await message.channel.send(message.content)
       # try
       #    evaluation = eval(message)
       #    ctx.send(evaluation)
       # except:
       #     return







async def setup(client):
    await client.add_cog(math(client))