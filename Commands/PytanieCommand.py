import discord
from discord.ext import commands
from random import choice
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandPytanie(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Pytanie(self, ctx, *, message):
        odpowiedzi = ['Tak', 'Nie', 'Możliwe', 'Raczej, Tak', 'Raczej, Nie']
        embed = discord.Embed(
            title='Odpowiedź',
            description=f'Pytanie: **{message}**\nOdpowiedź: **{choice(odpowiedzi)}**'
        )
        await ctx.send(embed=embed)

    @Pytanie.error
    async def pytanie_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}Pytanie <Tekst>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandPytanie(client))