import os
import discord
from discord.ext import commands
import random
from openai import OpenAI

oaitoken = os.getenv('oaitoken')
system_prompt = os.getenv('system_prompt')

ClientAi = OpenAI(api_key=oaitoken)

class Ai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ai.py success")

    @commands.command(aliases=['r','ai'])
    async def request(self, ctx, *, question):
        async with ctx.typing():
            question1 = str(question)
            response = ClientAi.chat.completions.create(
                model = 'gpt-4-0125-preview',
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user","content": question1 }
                ]
            )
            print(response)
            await ctx.send(response.choices[0].message.content[:2000])


    @commands.command()
    async def img(self, ctx, *, prompt):
        async with ctx.typing():
            prompt1 = str(prompt)
            generated_image = ClientAi.images.generate(
                model = 'dall-e-3',
                prompt = f"I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS: {prompt1}",
                size = "1792x1024",
                quality="hd",
                n=1,  
            )
            print(generated_image)
            image_url = generated_image.data[0].url
            await ctx.send(image_url)



async def setup(client):
    await client.add_cog(Ai(client))