import discord
from discord.ext import commands
from datetime import datetime
from json import load

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandUnmute(commands.Cog):

    @commands.command(manage_members=True)
    async def unmute(self, ctx, member: commands.MemberConverter):
        admin = ctx.message.author
        userAvatar = admin.avatar_url
        role = discord.utils.get(ctx.guild.roles, name="Zmutowany")
        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(
                title="Pomyślnie Odmutowano <a:greenbutton:876630840929566734>",
                color=discord.Colour.green(),
            )
            embed.add_field(name=f"Użytkownik:", value=f"{member.mention}")
            embed.set_footer(text=f'{admin}', icon_url=f"{userAvatar}")
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(
                title=f'<:warning:868110552268931114> Coś tu pomieszałeś, {ctx.author.name}.',
                description=f'Użytkownik: {member.mention} Nie Jest Zmutowany!',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}unmute <@member>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie » `{get_prefix(None, ctx)}unmute <@member>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(CommandUnmute(client))