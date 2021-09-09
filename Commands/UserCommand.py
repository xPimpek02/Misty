import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

def Returnembed(ctx=None, member=None):
    if ctx == None:
        role = member.roles
        role.reverse()
        created = str(member.created_at)
        joined = str(member.joined_at)
        embed = discord.Embed(
            title=f'Informacje Użytkownika',
            color=discord.Color.blue(),
            timestamp=datetime.utcnow(),
            description=f'''
                :bust_in_silhouette: • Nick: **{member}**

                :id: • ID: **{member.id}**

                🧾 • Ważność Konta: **{created[0: 16]}**
                
                <:PurplePlus:872813710769537054> • Dołączył: **{joined[0: 16]}**

                <:PurpleRole:872812810365698149> • Najwyższa Rola: **{role[0].mention}**
                '''
        )
        embed.set_thumbnail(url=member.avatar_url)
        return embed
    else:
        role = ctx.author.roles
        role.reverse()
        created = str(ctx.author.created_at)
        joined = str(ctx.author.joined_at)
        embed = discord.Embed(
            title=f'Informacje Użytkownika',
            color=discord.Color.blue(),
            timestamp=datetime.utcnow(),
            description=f'''
                        :bust_in_silhouette: • Nick: **{ctx.author}**

                        :id: • ID: **{ctx.author.id}**

                        🧾 • Ważność Konta: **{created[0: 16]}**

                        <:PurplePlus:872813710769537054> • Dołączył: **{joined[0: 16]}**

                        <:PurpleRole:872812810365698149> • Najwyższa Rola: **{role[0].mention}**
                        '''
        )
        embed.set_thumbnail(url=ctx.author.avatar_url)
        return embed

class CommandUser(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['userinfo'])
    async def user(self, ctx, member: discord.Member=None):
        if member:
            await ctx.send(embed=Returnembed(member=member))
            return
        await ctx.send(embed=Returnembed(ctx=ctx))

    @user.error
    async def user_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie: `{get_prefix(None, ctx.message)}user <@member/None>`',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandUser(client))