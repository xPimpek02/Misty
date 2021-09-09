import discord
from discord.ext import commands

class EventCommand_Error(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(EventCommand_Error(client))