import discord
from discord.ext import commands
from json import load, dump
from datetime import datetime
from time import sleep

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandLog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def logi(self, ctx, option, channel: discord.TextChannel):
        with open('Bases/log_channel.json', mode='r') as file:
            logchannel = load(file)
        if option == 'wlacz':
            logchannel[str(f"Server: {ctx.guild.id}")] = channel.id

            with open('Bases/log_channel.json', mode="w") as f:
                dump(logchannel, f, indent=4)
            embed = discord.Embed(
                color=discord.Color.from_rgb(255, 255, 255),
                timestamp=datetime.utcnow(),
                title='Ustawiono Kanał Logów Serwera <a:greenbutton:876630841567113236>',
            )
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif option == 'wylacz':
            with open('Bases/log_channel.json', mode="r") as f:
                channel = load(f)
            channel.pop(str(f"Server: {ctx.guild.id}"))

            with open('Bases/log_channel.json', mode="w") as f:
                dump(channel, f, indent=4)
            await ctx.send('Wylaczono Kanal!')

    @logi.error
    async def setlogi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}logi <wlacz/wylacz> <#kanal>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            if isinstance(error, commands.MissingRequiredArgument):
                embed = discord.Embed(
                    title='<:warning:868110552268931114> Wystąpił Błąd.',
                    description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}logi <wlacz/wylacz> <#kanal>`',
                    timestamp=datetime.utcnow(),
                    color=discord.Color.red()
                )
                embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            embed = discord.Embed(
                title='Użytkownik zmienił Nick',
                timestamp=datetime.utcnow(),
                color=discord.Color.from_rgb(128, 128, 128),
            )
            embed.add_field(name='<:offline:877268159638413343> Wcześniej', value=f'`{before.name}`')
            embed.add_field(name='<:pimpekrozpierdol:867544273276371005> Aktualnie', value=f'`{after.name}`')
            embed.set_footer(text=f'{after}', icon_url=after.avatar_url)
            with open('Bases/log_channel.json', mode="r") as f:
                Channel = load(f)
            for guild in self.client.guilds:
                for member in guild.members:
                    if int(after.id) == int(member.id):
                        try:
                            id = int(Channel[str(f"Server: {guild.id}")])
                            channel = self.client.get_channel(id)
                            await channel.send(embed=embed)
                        except:
                            pass

        if before.discriminator != after.discriminator:
            embed = discord.Embed(
                title = 'Użytkownik zmienił Tag',
                timestamp = datetime.utcnow(),
                color = discord.Color.from_rgb(128, 128, 128),
            )
            embed.add_field(name='<:offline:877268159638413343> Wcześniej', value=f'`{before}`')
            embed.add_field(name='<:pimpekrozpierdol:867544273276371005> Aktualnie', value=f'`{after}`')
            embed.set_footer(text=f'{after}', icon_url=after.avatar_url)

            with open('Bases/log_channel.json', mode="r") as f:
                Channel = load(f)
            for guild in self.client.guilds:
                for member in guild.members:
                    if int(after.id) == int(member.id):
                        try:
                            id = int(Channel[str(f"Server: {guild.id}")])
                            channel = self.client.get_channel(id)
                            await channel.send(embed=embed)
                        except:
                            pass

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if int(message.author.id) == int(self.client.user.id):
            return
        else:
            embed = discord.Embed(
                title='Wiadomość Została Usunięta',
                timestamp=datetime.utcnow(),
                color=discord.Color.from_rgb(128, 128, 128),
            )
            embed.add_field(name='<a:strzalka:868174820653801513> Treść Wiadomości', value=f'`{message.content}`')
            with open('Bases/log_channel.json', mode="r") as f:
                Channel = load(f)
            id = int(Channel[str(f"Server: {message.guild.id}")])
            channel = self.client.get_channel(id)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title='Użytkownik Dołączył <a:greenbutton:876630841567113236>',
            timestamp=datetime.utcnow(),
            color=discord.Color.green()
        )
        account = str(member.created_at)
        embed.add_field(name='<a:strzalka:868174820653801513> Nazwa', value=f'<:802985255874068490:867546845299212328> `{member}`')
        embed.add_field(name='<a:strzalka:868174820653801513> ID', value=f'<:802985255874068490:867546845299212328> `{member.id}`', inline=False)
        embed.add_field(name='<a:strzalka:868174820653801513> Konto', value=f'<:802985255874068490:867546845299212328> `{account[0: 19]}`', inline=False)
        with open('Bases/log_channel.json', mode="r") as f:
            Channel = load(f)
        id = int(Channel[str(f"Server: {member.guild.id}")])
        channel = self.client.get_channel(id)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = discord.Embed(
            title='Użytkownik Wyszedł <a:606562703917449226:867421579947933727>',
            timestamp=datetime.utcnow(),
            color=discord.Color.red()
        )
        account = str(member.created_at)
        embed.add_field(name='<a:strzalka:868174820653801513> Nazwa',
                        value=f'<:802985255874068490:867546845299212328> `{member}`')
        embed.add_field(name='<a:strzalka:868174820653801513> ID',
                        value=f'<:802985255874068490:867546845299212328> `{member.id}`', inline=False)
        embed.add_field(name='<a:strzalka:868174820653801513> Konto',
                        value=f'<:802985255874068490:867546845299212328> `{account[0: 19]}`', inline=False)
        with open('Bases/log_channel.json', mode="r") as f:
            Channel = load(f)
        id = int(Channel[str(f"Server: {member.guild.id}")])
        channel = self.client.get_channel(id)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.name == self.client.user.name:
            return
        if before.content != after.content:
            embed = discord.Embed(
                title='Wiadomość Została Zedytowana <a:greenbutton:876630841567113236>',
                timestamp=datetime.utcnow(),
                color=discord.Color.teal()
            )
            embed.set_author(name=after.author, icon_url=after.author.avatar_url)
            embed.add_field(name='<:offline:877268159638413343> Wcześniej', value=f'`{before.content}`')
            embed.add_field(name='<:pimpekrozpierdol:867544273276371005> Aktualnie', value=f'`{after.content}`', inline=False)
            with open('Bases/log_channel.json', mode="r") as f:
                Channel = load(f)
            id = int(Channel[str(f"Server: {after.guild.id}")])
            channel = self.client.get_channel(id)
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(CommandLog(client))