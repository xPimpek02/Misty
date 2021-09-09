import discord
from discord.ext import commands
import requests
import certifi
import urllib3
import asyncio
import random
import re
from bs4 import BeautifulSoup

class CommandBitcoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def Bitcoin(self, ctx):
        await ctx.reply('Zbieranie Wartości...', delete_after=1)
        try:
            url = 'https://www.worldcoinindex.com/coin/bitcoin'
            page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET', url)
            soup = BeautifulSoup(page.data, 'html.parser')
            bitcoin_price = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coinprice'}).text
            bitcoin_price = re.sub("[^0-9.,]", "", bitcoin_price)
            bitcoin_change = soup.find('div', attrs={'class': 'col-md-6 col-xs-6 coin-percentage'}).text
            bitcoin_change = re.sub("[^0-9.,%\-+]", "", bitcoin_change)
            embed = discord.Embed(
                title='Aktualny Kurs Bitcoina <:Bitcoin:868130551557656666>',
                description='Cena: {}$\nStatus: {}'.format(bitcoin_price, bitcoin_change),
                color=discord.Color.green()
            )
            embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.reply(embed=embed)
        except:
            embed = discord.Embed(
                title='<a:708338924250202183:867547679093817348> Wystąpił Problem.',
                description='Bot Napotkał Problem Podczas Zbierania Informacji. \nJeśli błąd będzie się powtarzał Skontaktuj się z Administracja.',
                color=discord.Color.orange()
            )
            await ctx.reply(embed=embed)
def setup(client):
    client.add_cog(CommandBitcoin(client))