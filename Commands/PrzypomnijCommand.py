import discord
from discord.ext import commands
from asyncio import sleep
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class DurationConverter(commands.Converter):
    async def convert(self, ctx, argument):
        amount = argument[:-1]
        unit = argument[-1]

        if amount.isdigit() and unit in ['s', 'm', 'h', 'd']:
            return (int(amount), unit)

        raise commands.BadArgument(message='Zła jednostka czasu')

class CommandPrzypomnij(commands.Cog):

    def __init__(self, client):
        self.multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        self.client = client

    @commands.command(aliases=['zapamietaj'])
    async def Przypomnij(self, ctx, duration: DurationConverter = 0, *, message):
        time = datetime.now().strftime("%H:%M:%S")
        user = ctx.message.author
        amount, unit = duration
        embed = discord.Embed(
            title='Ustawiono Przypomnienie!',
            color=discord.Color.random()
        )
        embed.add_field(name='Wiadomość »', value=f'`{message}`')
        embed.add_field(name='Przypomnienie Za »', value=f'`{amount}{unit}`', inline=False)
        embed.set_footer(text='Pamiętaj, aby mieć włączone Prywatne Wiadomości.')
        await ctx.send(embed=embed)
        await sleep(amount * self.multiplier[unit])
        embed=discord.Embed(
            title='Przypomnienie',
            timestamp=datetime.utcnow(),
            color=discord.Color.random()
        )
        embed.add_field(name=f'Wiadomość »', value=f'{message}', inline=False)
        embed.add_field(name='Serwer »', value=f'{ctx.guild.name}', inline=False)
        embed.add_field(name='Czas Utworzenia »', value=f'{time}')
        await user.send(embed=embed)

    @Przypomnij.error
    async def przypomnij_error(self, ctx, error):
        global get_prefix
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}Przypomnij <czas> <Tekst>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}Przypomnij <czas> <Tekst>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandPrzypomnij(client))