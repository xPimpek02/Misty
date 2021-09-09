import discord
from discord.ext import commands
from pyfiglet import figlet_format
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandAscii(commands.Cog):

    def init(self, client):
        self.client = client

    @commands.command(aliases=['figlet'])
    async def ascii(self, ctx, *, message, num=0):
        for letter in message:
            num += 1
        if num > 9:
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Tekst Nie Może mieć więcej niż 9 liter.',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(
            title='<a:strzalka:868174820653801513> Sformatowano!',
            timestamp=datetime.utcnow(),
            description=f'```{figlet_format(message)}```'''
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

    @ascii.error
    async def ascii_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}ascii <tekst>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandAscii(client))