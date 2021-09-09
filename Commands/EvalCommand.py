import discord
from discord.ext import commands
from aioconsole import aexec
import sys
import io
import inspect

class CommandEval(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eval(self, ctx, *, code):
        if int(ctx.author.id) == int(761705012719779890):
            res = eval(code)
            if inspect.isawaitable(res):
                await ctx.send(await res)
                return
            else:
                await ctx.send(res)
                return

def setup(client):
    client.add_cog(CommandEval(client))