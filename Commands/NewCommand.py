import discord
from discord.ext import commands

class CommandNew(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nowacmd(self, ctx):
        await ctx.send('Działa!')


def setup(client):
    client.add_cog(CommandNew(client))