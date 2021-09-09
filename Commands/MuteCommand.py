import discord
from discord.ext import commands
from json import load
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandMute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: commands.MemberConverter, *, reason='Brak'):
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

        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(
            title='<a:strzalka:868174820653801513> Pomyslnie Zmutowano!',
            color=discord.Color.from_rgb(69, 252, 63),
            timestamp=datetime.utcnow()
        )
        embed.add_field(name='Użytkownik:', value=f'<a:strzalka2:868175910426280027>{member.mention}')
        embed.add_field(name='Administrator:', value=f'<a:strzalka2:868175910426280027>{ctx.author.mention}', inline=False)
        embed.add_field(name='Powod:', value=f'<a:strzalka2:868175910426280027>{reason}', inline=False)
        embed.set_thumbnail(url=f'https://cdn.discordapp.com/emojis/868116099764473927.gif?v=1')
        await ctx.reply(embed=embed)


    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}mute <@member> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}mute <@member> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Kick_Members`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CommandMute(client))