import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient
from datetime import datetime
from json import load

cluster = MongoClient("mongodb+srv://pimpek:XaweSs55@cluster0.vaofm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
database = cluster["pimpek"]
collection = database["warns-base"]

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandWarn(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ostrzez'])
    @commands.has_permissions(manage_roles=True)
    async def warn(self, ctx, member: discord.Member, *, reason="Brak"):
        if member.top_role > ctx.author.top_role:
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Rola Użytkownika: {member.mention} Jest Wyższa Od Twojej.',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        id = member.id
        if collection.count_documents({"guild": ctx.guild.id, "memberid":member.id}) == 0:
            collection.insert_one({"guild": ctx.guild.id, "memberid": id, "warns": 0})
        warn_count = collection.find_one({"guild": ctx.guild.id, "memberid": id})
        count = warn_count["warns"]
        new_count = count + 1
        collection.update_one({"guild": ctx.guild.id, "memberid": id},{"$set":{"warns": new_count}})
        embed = discord.Embed(
            title='Pomyslnie Zwarnowano <a:greenbutton:876630840929566734>',
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=256))
        embed.add_field(name='Użytkownik', value=f'<a:strzalka:868174820653801513> {member.mention}', inline=False)
        embed.add_field(name='Powód', value=f'<a:strzalka:868174820653801513> `{reason}`', inline=False)
        embed.add_field(name='Warn', value=f'<a:strzalka:868174820653801513> `{new_count}`', inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(
            title='Otrzymałeś Warna <:warning:868110552268931114>',
            timestamp=datetime.utcnow(),
            color=discord.Color.red()
        )
        embed.set_footer(text=f'Ostrzeżenie: {new_count}')
        embed.add_field(name='Server', value=f'`{ctx.guild}`')
        embed.add_field(name='Administrator', value=f'`{ctx.author}`')
        embed.add_field(name='Powód', value=f'`{reason}`', inline=False)
        await member.send(embed=embed)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}warn <@member> <powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}warn <@member> <powód>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['warny', 'warns'])
    @commands.has_permissions(manage_roles=True)
    async def warnings(self, ctx, member: discord.Member):
        id = member.id
        if collection.count_documents({"guild": ctx.guild.id, "memberid": member.id}) == 0:
            collection.insert_one({"guild": ctx.guild.id, "memberid": id, "warns": 0})
        warn_count = collection.find_one({"guild": ctx.guild.id, "memberid": id})
        count = warn_count["warns"]
        embed = discord.Embed(
            title=f'Ostrzezenia: {member}',
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=256))
        embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Użytkownik', value=f'<a:strzalka:868174820653801513> {member.mention}', inline=False)
        embed.add_field(name='Warny', value=f'<a:strzalka:868174820653801513> `{count}`', inline=False)
        await ctx.send(embed=embed)

    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}warnings <@member>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Roles`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Roles`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def usunwarna(self, ctx, member: discord.Member, i):
        id = member.id
        if collection.count_documents({"guild": ctx.guild.id, "memberid": member.id}) == 0:
            collection.insert_one({"guild": ctx.guild.id, "memberid": id, "warns": 0})
        warn_count = collection.find_one({"guild": ctx.guild.id, "memberid": id})
        count = warn_count["warns"]
        if int(count) < int(i):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Podana osoba, nie posiada `{i}` lub więcej warnów.',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        count = int(count) - int(i)
        collection.update_one({"guild": ctx.guild.id, "memberid": id}, {"$set": {"warns": count}})
        embed = discord.Embed(
            title=f'Usunięto Warny <a:greenbutton:876630840929566734>',
            color=discord.Color.green(),
            timestamp=datetime.utcnow()
        )
        embed.set_thumbnail(url=ctx.guild.icon_url_as(size=256))
        embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Użytkownik', value=f'<a:strzalka:868174820653801513> {member.mention}', inline=False)
        embed.add_field(name='Usunięte Warny', value=f'<a:strzalka:868174820653801513> `{i}`', inline=False)
        await ctx.send(embed=embed)

    @usunwarna.error
    async def usunwarna_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}usunwarna <@member> <ilość>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}usunwarna <@member> <ilość>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Roles`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandWarn(client))