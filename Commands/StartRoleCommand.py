import discord
from discord.ext import commands
from json import load, dump
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandNazwa(commands.Cog):

    @commands.command(aliases=['startrole'])
    @commands.has_permissions(manage_roles=True)
    async def startowarola(self, ctx, rola: discord.Role):
        with open('Bases/startrole.json', mode="r") as f:
            eventrole = load(f)
        eventrole[str(f"Server: {ctx.guild.id}")] = rola.name

        with open('Bases/startrole.json', mode="w") as f:
            dump(eventrole, f, indent=4)
        embed = discord.Embed(
            title='Startowa Rola Zostala Ustawiona <:PurpleCheckmark:872811444079579157>',
            timestamp=datetime.utcnow(),
            color=discord.Color.blurple()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    @startowarola.error
    async def startowarola_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}startowarola <@rola>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}startowarola <@rola>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Roles`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CommandNazwa(client))