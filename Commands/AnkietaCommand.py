import discord
from discord.ext import commands
from json import load


def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandAnieta(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def ankieta(self, ctx, *, mess):
        embed = discord.Embed(
            title='Ankieta!',
            color=discord.Color.blurple()
        )
        embed.add_field(name="Temat:", value=f"{mess}")
        embed.set_footer(text=f"Organizator: {ctx.author.name}")
        anketa = await ctx.send(embed=embed)
        yes = self.client.get_emoji(863961564489973760)
        no = self.client.get_emoji(863980938166009887)
        await anketa.add_reaction(yes)
        await anketa.add_reaction(no)

    @ankieta.error
    async def ankieta_error(self, ctx, error):
        global get_prefix
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="» Odmowa dostępu «",
                description=f'Proszę podać tekst. \nPoprawne użycie `{get_prefix(ctx, ctx.message)}ankieta <tekst>`',
                color=discord.Colour.magenta(),
            )
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title="» Odmowa dostępu «",
                description=f'Proszę podać prawidłowy tekst.',
                color=discord.Colour.magenta(),
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandAnieta(client))