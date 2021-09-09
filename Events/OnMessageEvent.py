import discord
from discord.ext import commands
from json import load
from datetime import datetime
from re import search


class MessageEvent(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.url_regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        if message.author.guild_permissions.manage_messages:
            return
        with open('Bases/antylink.json', mode='r') as file:
            antylink = load(file)
        for key, value in antylink.items():
            try:
                if int(message.guild.id) == int(key):
                    msg = message.content.lower()
                    if search(self.url_regex, message.content):
                        embedchat = discord.Embed(
                            title='Wykryto Link <:warning:868110552268931114>',
                            description=f'{message.author} Próbował Wysłać Link!',
                            color=discord.Color.red(),
                            timestamp=datetime.utcnow()
                        )
                        await message.channel.send(embed=embedchat)
                        await message.delete()
                        author = message.author
                        embed = discord.Embed(
                            title='Ostrzezenie <a:708338924250202183:867547679093817348>',
                            description=f'Na Serwerze: **{message.guild}** Została nałożona blokada linków.\nTwoja Wiadomość: `{message.content}` została usunięta!',
                            color=discord.Color.red(),
                            datetime=datetime.utcnow()
                        )
                        await author.send(embed=embed)
                        break
            except:
                pass
def setup(client):
    client.add_cog(MessageEvent(client))