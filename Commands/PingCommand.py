import discord
from discord.ext import commands

class CommandPing(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Ping(self, ctx):
        await ctx.reply((f"Pong! {round(self.client.latency * 1000)}ms"), mention_author=False)

def setup(client):
    client.add_cog(CommandPing(client))