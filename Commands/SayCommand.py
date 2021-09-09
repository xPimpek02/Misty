import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class Commandpowiedz(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['say'])
    async def powiedz(self, ctx, *, message=None):
        if not message:
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx.message)}powiedz <tekst>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        await ctx.reply(message, mention_author=False, allowed_mentions=discord.AllowedMentions(
                                                        everyone=False, users=False, roles=False))

def setup(client):
    client.add_cog(Commandpowiedz(client))