import discord
from discord.ext import commands
from pymongo import MongoClient
from datetime import datetime
from json import load, dump

cluster = MongoClient("mongodb+srv://pimpek:XaweSs55@levele.m3s0g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

levele = cluster['discord']['levele']

class CommandLevels(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.mnoznik = 5

    @commands.command()
    async def ustawlvl(self, ctx, option, i=None, channel: discord.TextChannel=None):
        if option == 'wlacz':
            with open('Bases/levels_base.json', mode='r') as file:
                levels = load(file)
                try:
                    a = levels[str(ctx.guild.id)]
                    embed = discord.Embed(
                        title='<:warning:868110552268931114> Wystąpił Błąd.',
                        description=f'Levelowanie Już Jest Włączone',
                        timestamp=datetime.utcnow(),
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=embed)
                    return
                except:
                    levels[str(ctx.guild.id)] = True
                with open('Bases/levels_base.json', mode="w") as f:
                    dump(levels, f, indent=4)
                embed = discord.Embed(
                    title='Włączono Levelowanie <a:greenbutton:876630841567113236>',
                    color=discord.Color.green(),
                    timestamp=datetime.utcnow()
                )
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.reply(embed=embed, mention_author=False)
        elif option == 'wylacz':
            with open('Bases/levels_base.json', mode='r') as file:
                levels = load(file)
                try:
                    levels.pop(str(ctx.guild.id))
                    with open('Bases/levels_base.json', mode="w") as f:
                        dump(levels, f, indent=4)
                    embed = discord.Embed(
                        title='Wyłączono Levelowanie <a:606562703917449226:867421579947933727>',
                        color=discord.Color.red(),
                        timestamp=datetime.utcnow()
                    )
                    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.reply(embed=embed, mention_author=False)
                except:
                    embed = discord.Embed(
                        title='<:warning:868110552268931114> Wystąpił Błąd.',
                        description=f'Levelowanie Już Jest Wyłączone',
                        timestamp=datetime.utcnow(),
                        color=discord.Color.red()
                    )
                    await ctx.send(embed=embed)
                    return

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('Bases/levels_base.json', mode='r') as file:
            levels = load(file)
        try:
            if levels[str(message.guild.id)] != None:
                stats = levele.find_one({"Guild": message.guild.id, "id": message.author.id})
                if not message.author.bot:
                    if stats is None:
                        new_user = {"Guild": message.guild.id, "id": message.author.id, "xp": 100}
                        levele.insert_one(new_user)
                    else:
                        xp = stats["xp"] + 5
                        levele.update_one({"Guild": message.guild.id, "id": message.author.id}, {"$set":{"xp": xp}})
                        lvl = 0
                        while True:
                            if xp < ((50*(lvl**2))+(50*(lvl-1))) + 50:
                                break
                            lvl += 1
                        xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                        if xp == 0:
                            embed = discord.Embed(
                                title='Osiągnąłeś Następny Poziom <:dodatkowe2:868578908713406557>',
                                description=f'{message.author.mention}, Brawo osiągnąłeś następny Poziom: **{lvl}**',
                                color=discord.Color.purple(),
                                timestamp=datetime.utcnow()
                            )
                            embed.set_thumbnail(url=message.guild.icon_url)
                            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
        except:
            pass

    @commands.command()
    async def rank(self, ctx):
        with open('Bases/levels_base.json', mode='r') as file:
            levels = load(file)
        try:
            if levels[str(ctx.guild.id)] != None:
                stats = levele.find_one({"Guild": ctx.guild.id, "id": ctx.author.id})
                if stats is None:
                    embed = discord.Embed(description='Nie Uzyskales Jeszcze Żadnego Poziomu!', color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                xp = stats["xp"]
                lvl = 1
                rank = 0
                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * (lvl - 1))) + 50:
                        break
                    lvl += 1
                xp -= ((50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))) - 5
                boxes = int((xp/(50*((1/2) * lvl)))*5)
                boxes = int(boxes / 4 + 3)
                print(boxes)
                rankings = levele.find().sort("xp",-1)
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(
                    color=discord.Color.blurple(),
                    timestamp=datetime.utcnow()
                )
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed.add_field(name="Poziom", value=f'<:802985255874068490:867546845299212328> {lvl}', inline=True)
                embed.add_field(name="XP", value=f'<:802985255874068490:867546845299212328> {xp}/{int(200*((1/2)* lvl))}', inline=True)
                embed.add_field(name="Pasek Postępu", value=boxes * ":blue_square:" + (8-boxes) * ":white_large_square:", inline=False)
                await ctx.send(embed=embed)
        except:
            print('error')


def setup(client):
    client.add_cog(CommandLevels(client))