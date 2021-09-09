import discord
from discord.ext import commands
from discord.ext.commands import Cog
from json import load, dump
from datetime import datetime

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class CommandReactionRole(commands.Cog):


    def __init__(self, client):
        self.client = client


    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            pass
        else:
            with open('Bases/reactrole_base.json') as react_file:
                data = load(react_file)
                for key in data:
                    if key['emoji'] == payload.emoji.name and key['message_id'] == str(payload.message_id):
                        role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=key['role_id'])
                        await payload.member.add_roles(role)
                        guild = self.client.get_guild(payload.guild_id)
                        embed = discord.Embed(
                            title='Uzyskano Role <a:greenbutton:876630841567113236>',
                            color=discord.Color.green(),
                            timestamp=datetime.utcnow(),
                            description=f'Rola: `{role.name}`'
                        )
                        embed.set_thumbnail(url=guild.icon_url_as(size=64))
                        await payload.member.send(embed=embed)

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        with open('Bases/reactrole_base.json') as react_file:
            data = load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == str(payload.message_id):
                    role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

    @commands.command(aliases=['rr', 'reactrole'])
    @commands.has_permissions(manage_channels=True)
    async def reactionrole(self, ctx, kanal: discord.TextChannel, messageid, emoji, role: discord.Role):
        message = await kanal.fetch_message(messageid)
        await message.add_reaction(emoji)
        a = emoji
        licznik = 0
        emoji = emoji.replace("<", "").replace(">", "")
        for znak in emoji:
            if znak == ":":
                licznik += 1
            if licznik == 2:
                emoji = emoji.replace(f"{znak}", "")

        with open('Bases/reactrole_base.json') as json_file:
            data = load(json_file)


            new_react_role = {'role_name': role.name,
                              'role_id': role.id,
                              'emoji': emoji,
                              'message_id': messageid}

            data.append(new_react_role)

        with open('Bases/reactrole_base.json', 'w') as f:
            dump(data, f, indent=4)

        embed = discord.Embed(
            title='Utworzono ReactionRole <a:greenbutton:876630841567113236>',
            timestamp=datetime.utcnow(),
            description=f'''
**Kanal:** {kanal.mention}
**Rola:** {role.mention}
**Emoji:** {a}
''',
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @reactionrole.error
    async def reactionrole_erorr(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}reactionrole <#Kanal> <IDWiadomosci> <Emoji> <@Rola>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Poprawne Uzycie: `{get_prefix(None, ctx)}reactionrole <#Kanal> <IDWiadomosci> <Emoji> <@Rola>`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='<:warning:868110552268931114> Wystąpił Błąd.',
                description=f'Niestety, ale nie posiadasz permisji » `Manage_Channels`',
                timestamp=datetime.utcnow(),
                color=discord.Color.red()
            )
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CommandReactionRole(client))