import discord
from discord.ext import commands
from json import load
from discord.utils import get

class MemberJoinEvent(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            with open('Bases/startrole.json', mode="r") as f:
                Serwer = load(f)
                for a in Serwer:
                    if int(a.replace('Server: ', '')) == member.guild.id:
                        a = Serwer[str(f"Server: {member.guild.id}")]
                        for role in member.guild.roles:
                            if str(role.name) == str(a):
                                roleg = discord.utils.get(member.guild.roles, name=f"{a}")
                                await member.add_roles(roleg)
        except:
            pass

def setup(client):
    client.add_cog(MemberJoinEvent(client))