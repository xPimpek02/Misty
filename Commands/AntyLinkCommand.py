import discord
from discord.ext import commands
from json import load, dump
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class AntyLinkCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def antylink(self, ctx, option):
        if option == 'wlacz':
            with open('Bases/antylink.json', mode='r') as file:
                antylink = load(file)
            antylink[str(ctx.guild.id)] = True
            with open('Bases/antylink.json', mode="w") as f:
                dump(antylink, f, indent=4)
                embed = discord.Embed(
                    title='Uruchomiono AntyLink <a:greenbutton:876630840929566734>',
                    color=discord.Color.green(),
                    timestamp=datetime.utcnow()
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

        elif option == 'wylacz':
            with open('Bases/antylink.json', mode="r") as f:
                antylink = load(f)
            try:
                antylink.pop(str(ctx.guild.id))
            except:
                pass
            with open('Bases/antylink.json', mode="w") as f:
                dump(antylink, f, indent=4)
            embed = discord.Embed(
                title='Wylaczono AntyLink <a:606562703917449226:867421579947933727>',
                color=discord.Color.red(),
                timestamp=datetime.utcnow()
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @antylink.error
    async def anty_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}antylink <wlacz/wylacz>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}antylink <wlacz/wylacz>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `manage_messages`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(AntyLinkCommand(client))