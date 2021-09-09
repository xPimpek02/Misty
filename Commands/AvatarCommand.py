import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandNazwa(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Avatar(self, ctx, Member: discord.Member = None):
        if not Member:
            embed = discord.Embed(
                title=f'Avatar: {ctx.author.name}',
                color=discord.Color.teal()
            )
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(
            title=f'Avatar: {Member.name}',
            color=discord.Color.teal()
        )
        embed.set_image(url=Member.avatar_url)
        await ctx.send(embed=embed)


    @Avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title = '<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp = datetime.utcnow(),
                description = f'Poprawne Uzycie: `{get_prefix(None, ctx.message)}avatar <@member>`',
                color = discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandNazwa(client))