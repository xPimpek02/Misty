import discord
from discord.ext import commands
from datetime import datetime

class CommandBanList(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def banlist(self, ctx):
        bans = await ctx.guild.bans()
        pretty_list = ["<:802985255874068490:867546845299212328> {0.name}#{0.discriminator} | ID: {0.id}\n".format(entry.user) for entry in bans]
        banned_users = f'\n{"".join(pretty_list)}'
        embed = discord.Embed(
            title=f'Lista Banów: {ctx.guild.name}',
            timestamp=datetime.utcnow(),
            description=banned_users,
            color=discord.Color.gold()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @banlist.error
    async def banlist_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Ban_Members`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandBanList(client))