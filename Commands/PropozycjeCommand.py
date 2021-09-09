import discord
from discord.ext import commands
from datetime import datetime

class CommandPropozyje(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['propozycje'])
    async def Propozycja(self, ctx, *, tekst):
        channel = self.client.get_channel(879711539194630184)
        embed = discord.Embed(
            title='Nowa Propozycja <a:greenbutton:876630840929566734>',
            description=f'Serwer: `{ctx.guild.name}`\nOsoba: `{ctx.author}`\n```{tekst}```',
            timestamp=datetime.utcnow(),
            color=discord.Color.dark_theme()
        )
        await channel.send(embed=embed)
        embed = discord.Embed(
            title='Wysłano Propozycje <a:greenbutton:876630841567113236>',
            description=f'```{tekst}```',
            color=discord.Color.green(),
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text='Wysyłanie Propozycji Niedotyczących Bota będą karane Banem.')
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandPropozyje(client))