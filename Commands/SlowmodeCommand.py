import discord
from discord.ext import commands
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

class CommandSlowmode(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.multiplier = {'s': 1, 'm': 60, 'h': 3600}

    @commands.command(manage_messages=True)
    async def slowmode(self, ctx, time: DurationConverter):
        amount, unit = time
        try:
            await ctx.channel.edit(slowmode_delay=amount * self.multiplier[unit])
            embed = discord.Embed(
                title='Poprawnie Zaktualizowano Slowmode!',
                color=discord.Color.light_gray()
            )
            message = await ctx.send(embed=embed)
            emotka = self.client.get_emoji(863961893998821386)
            await message.add_reaction(emotka)
        except:
            embed = discord.Embed(
                title='Wystąpił Nieoczekiwany Błąd! <:blue:863966543221620816>',
                description='Podczas Wykonywania Komendy Wystąpił Błąd Sprawdź Czy',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.add_field(name='Nie Przekroczyłeś Dozwolnego Limitu:', value='Maksymalny Czas: 6h')
            embed.add_field(name='Podales Poprawna Jednostke:', value='1s, 1m, 1h', inline=False)
            await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}slowmode <czas>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
                )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='Wystąpił Nieoczekiwany Błąd! <:blue:863966543221620816>',
                description='Podczas Wykonywania Komendy Wystąpił Błąd Sprawdź Czy',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.add_field(name='Nie Przekroczyłeś Dozwolnego Limitu:', value='Maksymalny Czas: 6h')
            embed.add_field(name='Podales Poprawna Jednostke:', value='1s, 1m, 1h', inline=False)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandSlowmode(client))