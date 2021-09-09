import discord
from discord.ext import commands
from json import dump, load

class EventGuildRemove(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('Bases/prefixes_base.json', mode="r") as f:
            prefixes = load(f)
        prefixes.pop(str(guild.id))

        with open('Bases/prefixes_base.json', mode="w") as f:
            dump(prefixes, f, indent=4)
        channel = self.client.get_channel(879711539194630184)
        embed = discord.Embed(
            title='Misty Wyszedł z Serwera <a:verify:863961893998821386>',
            description=f'Serwer: `{guild.name}`\nID: `{guild.id}`\nAktualne Serwery: `{str(len(self.client.guilds))}`',
            color=discord.Color.red()
        )
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(EventGuildRemove(client))