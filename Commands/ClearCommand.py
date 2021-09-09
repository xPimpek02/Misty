import discord
from discord.ext import commands
from json import load
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandClear(commands.Cog):

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, times=10):
        if times > 1000:
            embed = discord.Embed(
                title='Wystąpił Nieoczekiwany Błąd <:cross1:863972481907294229>',
                description=f'Przekroczono Limit! {times}/1000',
                color=discord.Color.red()
            )

            await ctx.reply(embed=embed, mention_author=False)
            return
        await ctx.channel.purge(limit=times)
        embed = discord.Embed(
            title='*Usunięto Wiadomości*',
            description=f'Pomyslnie Usunięto ▸ **{times}**, Ostatnich Wiadomości',
            color=discord.Color.dark_grey()
        )
        embed.set_footer(text=f'By {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}clear <liczba>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}clear <liczba>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Messages`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandClear(client))