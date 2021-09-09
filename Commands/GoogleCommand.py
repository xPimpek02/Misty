import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class GoogleCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx, *, message):
        message = message.replace(' ', '+')
        embed = discord.Embed(
            description=f'[GOOGLE](https://letmegooglethat.com/?q={message})',
            color=discord.Color.light_grey(),
            timestamp=datetime.utcnow()
        )
        await ctx.reply(embed=embed, mention_author=False)

    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}Google <tekst>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
def setup(client):
    client.add_cog(GoogleCommand(client))