import discord
from discord.ext import commands
from json import load, dump
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]


class CommandSetPrefix(commands.Cog):

    @commands.command(aliases=['prefix'])
    @commands.has_permissions(manage_channels=True)
    async def setprefix(self, ctx, prefix):
        with open('Bases/prefixes_base.json', mode="r") as f:
            prefixes = load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open('Bases/prefixes_base.json', mode="w") as f:
            dump(prefixes, f, indent=4)
        embed = discord.Embed(
            title='Powodzenie! <a:verify:863961893998821386>',
            description=f'Pomyslnie Ustawiono Prefix na: `{prefix}`',
            color=discord.Color.green()
        )
        await ctx.reply(embed=embed, mention_author=False)

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji: `Manage Channels`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie: `{get_prefix(None, ctx.message)}setprefix <prefix>`',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandSetPrefix(client))