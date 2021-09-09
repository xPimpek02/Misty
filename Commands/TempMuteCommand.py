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


class CommandTempMute(commands.Cog):

    def __init__(self, client):
        self.client = client
        # Pass

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempmute(self, ctx, member: commands.MemberConverter, *, duration: DurationConverter, reason="Brak"):
        multiplier = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
        amount, unit = duration
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Zmutowany")

        if not mutedRole:
            embed = discord.Embed(
                title='<a:loading:868178388270055454> Jeszcze Chwilka!',
                description='`Na Serwerze Nie Zostala Znaleziona Rola: Zmutowany`\n`Jestem W Trakcie Tworzenia, oraz ustawienia uprawnień.`',
                color=discord.Color.red()
            )
            embed.set_footer(text='Czas Oczekiwania Jest Zależny Od ilości Kanałów Na Serwerze!')
            await ctx.send(embed=embed, delete_after=4)
            mutedRole = await guild.create_role(name="Zmutowany")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False)


        await member.add_roles(mutedRole)
        embed = discord.Embed(
            title='<a:strzalka:868174820653801513> Pomyslnie Zmutowano!',
            color=discord.Color.green()
        )
        embed.add_field(name='Użytkownik: ', value=f'<a:strzalka2:868175910426280027>{member.mention}', inline=False)
        embed.add_field(name='Administrator: ', value=f'<a:strzalka2:868175910426280027>{ctx.author.mention}', inline=False)
        embed.add_field(name='Czas: ', value=f'<a:strzalka2:868175910426280027>{amount}{unit}')
        embed.add_field(name='Powod: ', value=f'<a:strzalka2:868175910426280027>{reason}')
        embed.set_thumbnail(url=member.avatar_url_as(size=128))
        await ctx.send(embed=embed)
        await sleep(amount * multiplier[unit])
        await member.remove_roles(mutedRole)

    @tempmute.error
    async def tempmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}tempmute <@member> <czas> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}tempmute <@member> <czas> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandTempMute(client))