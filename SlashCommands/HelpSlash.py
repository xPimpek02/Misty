import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class HelpSlash(commands.Cog):

    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(
        name='help',
        description='Informacje Komend. | /help <komenda>',
        options=[create_option(
                name='option',
                description='Pomogę ci w wybranej komendzie.',
                required=True,
                option_type=3,
                choices=[
                    create_choice(name='Ban', value='kban'),
                    create_choice(name='BanID', value='kbanid'),
                    create_choice(name='TempBan', value='ktempban'),
                    create_choice(name='Banlist', value='kbanlist'),
                    create_choice(name='Unban', value='kunban'),
                    create_choice(name='Kick', value='kkick'),
                    create_choice(name='Mute', value='kmute'),
                    create_choice(name='Tempmute', value='ktempmute'),
                    create_choice(name='Clear', value='kclear'),
                    create_choice(name='Slowmode', value='kslowmode'),
                    create_choice(name='DodajEmoji', value='kdodajemoji'),
                    create_choice(name='Warn', value='kwarn'),
                    create_choice(name='Usunwarna', value='kusunwarna'),
                    create_choice(name='Warnings', value='kwarnings'),
                ])])

    async def _help(self, ctx: SlashContext, option: str):
        if option == 'kwarnings':
            embed = discord.Embed(
                title='Informacje Komendy: Warnings',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Warnings <@member>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_roles`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kusunwarna':
            embed = discord.Embed(
                title='Informacje Komendy: Usunwarna',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Usunwarna <@member> <ilość>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_roles`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kwarn':
            embed = discord.Embed(
                title='Informacje Komendy: Warn',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Warn <@member> <Powód>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_roles`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kdodajemoji':
            embed = discord.Embed(
                title='Informacje Komendy: DodajEmoji',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}DodajEmoji <link> <Nazwa>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_emojis`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kslowmode':
            embed = discord.Embed(
                title='Informacje Komendy: Slowmode',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Slowmode <czas>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_messages`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kclear':
            embed = discord.Embed(
                title='Informacje Komendy: Clear',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Clear <Liczba>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`Manage_messages`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'ktempmute':
            embed = discord.Embed(
                title='Informacje Komendy: Tempmute',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Tempmute <@member> <Czas> <powód>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`kick_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kmute':
            embed = discord.Embed(
                title='Informacje Komendy: Mute',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}mute <@member> <powód>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`kick_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kkick':
            embed = discord.Embed(
                title='Informacje Komendy: Kick',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Kick <@member> <powód>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`kick_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kbanlist':
            embed = discord.Embed(
                title='Informacje Komendy: TempBan',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}banlist`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`ban_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'ktempban':
            embed = discord.Embed(
                title='Informacje Komendy: TempBan',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}Tempban <@member> <czas> <powód>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`ban_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kunban':
            embed = discord.Embed(
                title='Informacje Komendy: Unban',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}unban <id>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`ban_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kban':
            embed = discord.Embed(
                title='Informacje Komendy: Ban',
                timestamp=datetime.utcnow()
                )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}ban <@member> <powod>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`ban_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if option == 'kbanid':
            embed = discord.Embed(
                title='Informacje Komendy: BanID',
                timestamp=datetime.utcnow()
            )
            embed.add_field(name='Poprawne Uzycie', value=f'`{get_prefix(None, ctx)}banid <id> <powod>`')
            embed.add_field(name='Wymagane Uprawnienia', value=f'`ban_members`', inline=False)
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(HelpSlash(client))