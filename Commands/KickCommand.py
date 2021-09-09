import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandKick(commands.Cog):

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Brak"):
        if member == ctx.author:
            embed = discord.Embed(
                title='<a:606562703917449226:867421579947933727> Błąd!',
                timestamp=datetime.utcnow(),
                description=f'**Nie możesz Wyrzucić samego siebie!**',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        try:
            await ctx.guild.kick(member)
        except:
            embed = discord.Embed(
                title='<a:606562703917449226:867421579947933727> Wystąpił Nieoczekiwany Błąd!',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.add_field(name='*Możliwa Lista Powodów »*', value='▸ Rola Bota Jest Niższa Od Oznaczonej Osoby.\n▸ Próbujesz Wyrzucić Właściciela Serwera.')
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(
            title='Pomyślnie Wyrzucono <a:verifygreen:864205806127153152>',
            timestamp=datetime.utcnow(),
            color=discord.Colour.green()
        )
        embed.add_field(name="Powód:", value=f"`{reason}`", inline=False)
        embed.add_field(name="Użytkownik:", value=f"`{member}`", inline=False)
        embed.add_field(name="Administrator:", value=f"`{ctx.author}`")
        await ctx.channel.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie » `{get_prefix(None, ctx.message)}kick <@member> <Powód>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Poprawne Użycie » `{get_prefix(None, ctx.message)}kick <@member> <Powód>`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                timestamp=datetime.utcnow(),
                description=f'Niestety, ale nie posiadasz permisji » `Kick_Members`',
                color=discord.Color.red()
            )
            embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandKick(client))