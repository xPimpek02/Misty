import discord
from discord.ext import commands
from asyncio import sleep
from json import load
from datetime import datetime


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

class CommandTempban(commands.Cog):

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: commands.MemberConverter, duration: DurationConverter, reason="Brak"):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration
        await member.ban(reason=reason)
        embed = discord.Embed(
            title=f'Pomyslnie Zbanowano <a:greenbutton:876630841567113236>',
            timestamp=datetime.utcnow(),
            color=discord.Colour.green()
        )
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name=f"Użytkownik:", value=f'`{member}`')
        embed.add_field(name=f"Czas:", value=f'`{amount}{unit}`')
        embed.add_field(name=f"Powód:", value=f'`{reason}`', inline=False)
        await ctx.send(embed=embed)
        await sleep(amount * multiplier[unit])
        await ctx.guild.unban(member)
        embed = discord.Embed(
            title='Pomyslnie Odbanowano <a:greenbutton:876630841567113236>',
            color=discord.Color.green(),
            timestamp=datetime.utcnow(),
            description=f'Użytkownik: **{member}**'
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @tempban.error
    async def tempban_error(self, ctx, error):
        global get_prefix
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}TempBan <@member> <czas> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}TempBan <@member> <czas> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandTempban(client))