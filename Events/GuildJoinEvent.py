import discord
from discord.ext import commands
from json import dump, load

class EventGuildRemove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('Bases/prefixes_base.json', mode="r") as f:
            prefixes = load(f)
        prefixes[str(guild.id)] = '!'

        with open('Bases/prefixes_base.json', mode="w") as f:
            dump(prefixes, f, indent=4)
        channel = self.client.get_channel(879711539194630184)
        embed = discord.Embed(
            title='Misty Dołączył Na Serwer <a:verify:863961893998821386>',
            description=f'Serwer: `{guild.name}`\nID: `{guild.id}`\nAktualne Serwery: `{str(len(self.client.guilds))}`',
            color=discord.Color.blurple()
        )
        await channel.send(embed=embed)
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send('Cześć Jestem Misty, Dziękuje za Dodanie. Pamiętaj, aby przenieść moją Role do Góry inaczej mogę nie działać :(')
                break


def setup(client):
    client.add_cog(EventGuildRemove(client))