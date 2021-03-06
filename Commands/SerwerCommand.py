import discord
from discord.ext import commands
from datetime import datetime


class CommandSerwer(commands.Cog):

    @commands.command(aliases=['serverinfo', 'server', 'serwerinfo'])
    async def Serwer(self, ctx):
        guild = str(ctx.guild.created_at)
        embed = discord.Embed(
            title=f'π INFORMACJE SERWERA',
            timestamp=datetime.utcnow(),
            description=f'''
π β’ ZaΕoΕΌyciel: **{ctx.guild.owner.name}**
ββ
π β’ Nazwa Serwera: **{ctx.guild.name}**
ββ
:id: β’ Serwer ID: **{ctx.guild.id}**
ββ
ποΈ β’ Stworzony: **{guild[0: 16]}**
ββ
<a:nitro:868176846431338536> β’ Boosty: **{ctx.guild.premium_subscription_count}**
ββ
π₯ β’ Osoby: **{sum(not member.bot for member in ctx.guild.members)}**
ββ
πΎ β’ Boty: **{sum(member.bot for member in ctx.guild.members)}**
ββ
π β’ KanaΕy: **{len(ctx.guild.text_channels + ctx.guild.voice_channels)}**
ββ
π« β’ Role: **{len(ctx.guild.roles) -1}**
''',
            color=discord.Color.purple()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandSerwer(client))