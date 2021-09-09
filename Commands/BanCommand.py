import discord
from discord.ext import commands
from datetime import datetime
from random import choice
from json import load

gifs = ["https://cdn.discordapp.com/attachments/761708541307519026/863579359583272990/tenor_1.gif", "https://cdn.discordapp.com/attachments/761708541307519026/863564677706285066/tenor.gif"]

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Brak"):
        embed = discord.Embed(
            title=f'Pomyslnie Zbanowano <a:greenbutton:876630841567113236>',
            timestamp=datetime.utcnow(),
            color=discord.Colour.green()
        )
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name=f"Użytkownik:", value=f'`{member}`')
        embed.add_field(name=f"Powód:", value=f'`{reason}`')
        await ctx.channel.send(embed=embed)
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}ban <@member> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}ban <@member> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def banid(self, ctx, id, *, reason="Brak"):
        admin = ctx.message.author
        userAvatar = admin.avatar_url
        user = await self.client.fetch_user(id)
        banned_members = await ctx.guild.bans()
        for member in banned_members:
            for info in member:
                if str(info) == str(user):
                    embed = discord.Embed(
                        title='<:warning:868110552268931114> Wystąpił Błąd.',
                        description=f'{user.id} Posiada Już Bana!',
                        timestamp=datetime.utcnow(),
                        color=discord.Color.red()
                    )
                    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                    return
        await ctx.guild.ban(user)
        embed = discord.Embed(
            title=f'Pomyslnie Zbanowano <a:greenbutton:876630841567113236>',
            timestamp=datetime.utcnow(),
            color=discord.Colour.green()
        )
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name=f"Użytkownik:", value=f'`{user}`')
        embed.add_field(name=f"Powód:", value=f'`{reason}`')
        await ctx.channel.send(embed=embed)

    @banid.error
    async def banid_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}banid <id> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}banid <id> <Powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Ban_Members`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandBan(client))