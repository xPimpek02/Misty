import discord
from discord.ext import commands

class CommandInvites(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['invites'])
    async def Zaproszenia(self, ctx, member: discord.Member=None):
        totalInvites = 0
        if member == None:
            for i in await ctx.guild.invites():
                if i.inviter == ctx.author:
                    totalInvites += i.uses
            embed = discord.Embed(
                title=f'Twoje Zaproszenia: {totalInvites}',
                description=f'Serwer: `{ctx.guild.name}`',
                color=discord.Color.from_rgb(197, 187, 175)
            )
            await ctx.send(embed=embed)
        else:
            for i in await ctx.guild.invites():
                if i.inviter == member:
                    totalInvites += i.uses
            embed = discord.Embed(
                title=f'Zaproszenia: {totalInvites}',
                description=f'Serwer: `{ctx.guild.name}`\nOsoba: `{member}`',
                color=discord.Color.from_rgb(197, 187, 175)
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandInvites(client))