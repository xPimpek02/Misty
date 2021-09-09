import discord
from discord.ext import commands
from random import randint

class CommandWzium(commands.Cog):

    @commands.command()
    async def Wzium(self, ctx):
        await ctx.send(f'Masz {randint(1, 100)} Wziuma!')

def setup(client):
    client.add_cog(CommandWzium(client))