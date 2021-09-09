import discord
from discord.ext import commands
import requests
from io import BytesIO
from aiohttp import ClientSession
from json import load
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandAnimals(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pies(self, ctx):
        r = requests.get('https://no-api-key.com/api/v1/animals/dog')
        json_data = r.json()
        image_url = json_data['image']
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 133, 128)
        )
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        r = requests.get('https://no-api-key.com/api/v1/animals/panda')
        json_data = r.json()
        image_url = json_data['image']
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 133, 128)
        )
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def kot(self, ctx):
        r = requests.get('https://no-api-key.com/api/v1/animals/cat')
        json_data = r.json()
        image_url = json_data['image']
        embed = discord.Embed(
            color=discord.Color.from_rgb(255, 133, 128)
        )
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def captcha(self, ctx, *, tekst):
        async with ClientSession() as session:
            async with session.get(f'https://api.no-api-key.com/api/v2/recaptcha?text={tekst}') as resp:
                if resp.status != 200:
                    return
                data = BytesIO(await resp.read())
                await ctx.channel.send(file=discord.File(data, 'cool_image.png'))

    @captcha.error
    async def captcha_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}Captcha <tekst>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def simp(self, ctx, *, member: discord.Member):
        async with ClientSession() as session:
            async with session.get(f'https://api.no-api-key.com/api/v2/simpcard?image={member.avatar_url}') as resp:
                if resp.status != 200:
                    return
                data = BytesIO(await resp.read())
                await ctx.reply(file=discord.File(data, 'cool_image.png'), mention_author=False)

    @simp.error
    async def simp_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}Simp <@Member>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


    @commands.command()
    async def trash(self, ctx, *, member: discord.Member):
        async with ClientSession() as session:
            async with session.get(f'https://api.no-api-key.com/api/v2/trash?image={member.avatar_url}') as resp:
                if resp.status != 200:
                    return
                data = BytesIO(await resp.read())
                await ctx.reply(file=discord.File(data, 'cool_image.png'), mention_author=False)
    @trash.error
    async def trash_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}trash <@Member>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(CommandAnimals(client))