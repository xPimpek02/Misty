import discord
from discord.ext import commands
import requests

class CommandMeme(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        r = requests.get('https://ivall.pl/memy')
        json_data = r.json()
        image_url = json_data['url']
        embed = discord.Embed(
            title='O To Twój Mem!',
            color=discord.Color.blurple()
        )
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandMeme(client))