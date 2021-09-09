import discord
from discord.ext import commands
from json import load
from discord_buttons_plugin import *

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class MentionEvent(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.buttons = ButtonsClient(client)

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.client.user.mentioned_in(message):
            if message.reference is not None:
                return
            if message.content.startswith('<'):
                embed = discord.Embed(
                    title=f'Hi, im Misty',
                    color=discord.Color.green(),
                    description=f'My Prefix is: `{get_prefix(None, message)}`'
                )
                embed.set_image(url=message.author.avatar_url)
                embed.set_footer(text='Authors: Pimpek02#4098, QdliK#1234')
                await self.buttons.send(
                    content=None,
                    embed=embed,
                    channel=message.channel.id,
                    components=[
                        ActionRow([
                            Button(
                                style=ButtonType().Link,
                                label="Strona",
                                url="https://mistybot.pl"
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
    client.add_cog(MentionEvent(client))