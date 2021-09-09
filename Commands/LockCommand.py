import discord
from discord.ext import commands
from datetime import datetime

class CommandLock(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['zablokuj'])
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrite.view_channel == False:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
        embed = discord.Embed(title='Zablokowano Kanał <a:606562703917449226:867421579947933727>', color=discord.Color.red())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Channels`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['odblokuj'])
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        if overwrite.view_channel == False:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=False)
        else:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
        embed = discord.Embed(title='Odblokowano Kanał <a:greenbutton:876630840929566734>', color=discord.Color.green())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Channels`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CommandLock(client))