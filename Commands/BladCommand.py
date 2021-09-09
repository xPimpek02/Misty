import discord
from discord.ext import commands
from datetime import datetime
from discord.utils import get

class CommandBlad(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['zglosblad'])
    async def blad(self, ctx, *, message):
        embed = discord.Embed(
            title='Pomyslnie Zgłoszono Błąd!',
            color=discord.Color.green(),
            description=f'Błąd `{message}` Został Wysłany Do Administratorów.'
        )
        embed.set_footer(text='Wysyłanie Wiadomości Niedotyczących Błędów Bota będą karane, Banem.')
        await ctx.reply(embed=embed, mention_author=False)
        channel = self.client.get_channel(877612551314227230)
        embed = discord.Embed(
            title='Zgłoszenie Błędu!',
            description=f'```{message}```',
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='Server', value=f'Nazwa: `{ctx.guild}`\nID: `{ctx.guild.id}`', inline=False)
        embed.add_field(name='Przez', value=f'`{ctx.author}`')
        await channel.send(embed=embed)
        await channel.send('@everyone')

def setup(client):
    client.add_cog(CommandBlad(client))