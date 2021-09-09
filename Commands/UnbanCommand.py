import discord
from discord.ext import commands
from json import load
from datetime import datetime


def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

def Returnembed(ctx, member, ch):
    if ch == 1:
        embed = discord.Embed(
            title='Pomyslnie Odbanowano <a:greenbutton:876630841567113236>',
            color=discord.Color.green(),
            timestamp=datetime.utcnow(),
            description=f'Użytkownik: **{member}**'
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        return embed
    else:
        embed = discord.Embed(
            title='Nie odnaleziono Użytkownika <a:606562703917449226:867421579947933727>',
            description=f'Osoba: **{member}** Nie Posiada Bana!',
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        return embed


class CommandUnban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unban(self, ctx, *, member):
        banned_members = await ctx.guild.bans()
        try:
            member = int(member)
            try:
                user = await self.client.fetch_user(member)
                await ctx.guild.unban(user)
                await ctx.reply(embed=Returnembed(ctx, user, 1), mention_author=False)
                return
            except:
                await ctx.reply(embed=Returnembed(ctx, member, 2), mention_author=False)
                return
        except:
            for banned_member in banned_members:
                for info in banned_member:
                    if info != None:
                        if member == str(info):
                            await ctx.guild.unban(banned_member.user)
                            await ctx.reply(embed=Returnembed(ctx, member, 1), mention_author=False)
                            return
            await ctx.reply(embed=Returnembed(ctx, member, 2), mention_author=False)
            return
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}unban <nick#1234/MemberID>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}unban <nick#1234/MemberID>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandUnban(client))