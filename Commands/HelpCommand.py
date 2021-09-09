import discord
from discord.ext import commands
from datetime import datetime
from json import load
from discord_buttons_plugin import *

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandHelp(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.buttons = ButtonsClient(client)

    @commands.command()
    async def help(self, ctx):
        p = get_prefix(ctx, ctx.message)
        embed = discord.Embed(
            title='Spis Wszystkich Komend',
            description=f'Aktualny Prefix: `{p}`\nWszystkie Komendy: `45`',
            color=discord.Color.blurple(),
            timestamp=datetime.utcnow()
        )
        embed.add_field(name='<:tak:868516322571608116> • Administracyjne (16)', value='''
`Ban`, `Banid`, `TempBan`, `Banlist`, `Unban`, `Kick`, `Mute`, `Tempmute`, `Clear`, `Slowmode`, `dodajemoji`, `warn`, `warnings`, `usunwarna`, `lock`, `unlock`
''')
        embed.add_field(name='<:PurpleLink:872813473183203420> • Ustawienia (5)', value='''
`prefix`, `startowarola`, `logi`, `Antylink`, `ReactionRole`
        ''', inline=False)
        embed.add_field(name='<:dodatkowe:868529567386705931> • Dodatkowe (12)', value='''
`Przypomnij`, `Bitcoin`, `Ankieta`, `Ping`, `Serwer`, `Avatar`, `zglosblad`, `propozycja`, `giveaway`, `Userinfo`, `Regulamin`, `Zaproszenia`
''', inline=False)
        embed.add_field(name='<a:tak232:868530112717533204> • ForFun (12)', value='''
`Wzium`, `Powiedz`, `Ascii`, `Pytanie`, `Google`, `Meme`, `Kot`, `Pies`, `Simp`, `Trash`, `Captcha`, `Panda`
''', inline=False)
        embed.add_field(name='||~~<:PurpleVoice:872812888677548032> • Muzyka (8)~~|| Podczas Naprawy', value='''
`Play`, `Join`, `Disconnect`, `Skip`, `Pause`, `Resume`, `Search`, `Queue`
''')

        embed.set_footer(text=f'{ctx.author} | /help <komenda>', icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=64))
        await self.buttons.send(
            content = None,
            embed = embed,
            channel = ctx.channel.id,
            components = [
                ActionRow([
                    Button(
                        style = ButtonType().Link,
                        label = "Strona",
                        url = "https://mistybot.pl"
                    ),
                    Button(
                        style=ButtonType().Link,
                        label="Zaproszenie",
                        url="https://discord.com/oauth2/authorize?client_id=868497099279446027&permissions=8&scope=bot%20applications.commands"
                    ),
                    Button(
                        style=ButtonType().Link,
                        label="Discord Support",
                        url="https://discord.gg/8XKRdQae3M")

                ])
            ]
        )


def setup(client):
    client.add_cog(CommandHelp(client))