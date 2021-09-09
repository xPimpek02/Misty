import discord
from discord.ext import commands
from datetime import datetime


class CommandSerwer(commands.Cog):

    @commands.command(aliases=['serverinfo', 'server', 'serwerinfo'])
    async def Serwer(self, ctx):
        guild = str(ctx.guild.created_at)
        embed = discord.Embed(
            title=f'📑 INFORMACJE SERWERA',
            timestamp=datetime.utcnow(),
            description=f'''
👑 • Założyciel: **{ctx.guild.owner.name}**
━━
📃 • Nazwa Serwera: **{ctx.guild.name}**
━━
:id: • Serwer ID: **{ctx.guild.id}**
━━
🗓️ • Stworzony: **{guild[0: 16]}**
━━
<a:nitro:868176846431338536> • Boosty: **{ctx.guild.premium_subscription_count}**
━━
👥 • Osoby: **{sum(not member.bot for member in ctx.guild.members)}**
━━
👾 • Boty: **{sum(member.bot for member in ctx.guild.members)}**
━━
📋 • Kanały: **{len(ctx.guild.text_channels + ctx.guild.voice_channels)}**
━━
🎫 • Role: **{len(ctx.guild.roles) -1}**
''',
            color=discord.Color.purple()
        )
        embed.set_footer(text=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandSerwer(client))