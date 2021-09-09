import discord
from discord.ext import commands
from asyncio import sleep
from random import choice
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

class CommandGiveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(manage_channels=True, aliases=['konkurs'])
    async def giveaway(self, ctx, time: DurationConverter, *, prize):
        multiplier = {'s': 1, 'm': 60}
        amount, unit = time
        now = datetime.utcnow()
        embed = discord.Embed(
            title='Giveaway!',
            description=f'\n**Nagroda:** `{prize}`\n**Koniec Za:** `{amount}{unit}`\n> *Zaznacz Reakcje Aby Dołaczyć Do Konkursu!*',
            color=discord.Color.from_rgb(127, 233, 184),
            timestamp=now
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        message = await ctx.send(embed=embed)
        await message.add_reaction('🎉')
        await sleep(amount * multiplier[unit])
        new_message = await ctx.channel.fetch_message(message.id)
        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        if len(users) == 0:
            await ctx.send('Nikt Nie Wygrał ;(')
            return
        winner = choice(users)
        await ctx.send(f'Gratulacje, {winner.mention} Zdobywasz: {prize}')

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}giveaway <czas> <nagroda>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}giveaway <czas> <nagroda>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji: `Manage Channels`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandGiveaway(client))