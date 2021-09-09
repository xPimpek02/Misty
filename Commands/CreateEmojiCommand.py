from io import BytesIO

import discord
from discord.ext import commands
import aiohttp
from dotenv import load_dotenv
from json import load
from datetime import datetime


def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandCreateEmoji(commands.Cog):

    def init(self, client):
        self.client = client

    @commands.command(aliases=['dodajemoji', 'stworzemoji', 'dodajemotke', 'stworzemotke'])
    @commands.has_permissions(manage_emojis=True)
    async def createemoji(self, ctx, url: str, *, name):
        load_dotenv()
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        if r.headers['content-type'] == "image/gif":
                            emoji = f'<a:{name}:{emoji.id}>'
                        else:
                            emoji = f'<:{name}:{emoji.id}>'
                            embed = discord.Embed(
                                title=f'Dodano Emoji <a:rysujacy_sie_ptaszek:868116099764473927>',
                                description=f'**Poprawnie Dodano Emotke** • {emoji}',
                                color=discord.Color.from_rgb(100, 235, 32)
                            )

                        await ctx.send(embed=embed)
                        await ses.close()
                    else:
                        await ctx.send(f'Error when making request | {r.status} response.')
                        await ses.close()

                except discord.HTTPException:
                    await ctx.send('File size is too big!')

    @createemoji.error
    async def createemoji_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie » `{get_prefix(None, ctx.message)}dodajemoji <emoji-link> <nazwa>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie » `{get_prefix(None, ctx.message)}dodajemoji <emoji-link> <nazwa>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Emojis`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandCreateEmoji(client))
