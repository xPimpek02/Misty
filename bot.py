import discord
from discord.ext import commands, ipc
from json import load
from os import listdir
from discord_slash import SlashCommand, SlashContext
from datetime import datetime
from discord.ext import commands

def get_prefix(ctx, message):
    with open('Bases/prefixes_base.json', mode="r") as f:
        prefixes = load(f)
    return prefixes[str(message.guild.id)]

class Client(commands.Bot):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.ipc = ipc.Server(self,secret_key = "Swas")

    async def on_ready(self):
        licznik = 0
        for guild in client.guilds:
            for member in guild.members:
                licznik += 1
        print(f"""
            ━━━━› Misty ‹━━━━
            Pomyslnie Uruchomiono {client.user.name}
            Bot Autorstwa: Pimpek, Qdlik
            ID: {client.user.id}
            Servery: {str(len(client.guilds))}
            Osoby: {licznik}
              ━━━━━━━━━━━━━""")

    async def on_ipc_ready(self):
        print("Ipc server is ready.")

    async def on_ipc_error(self, endpoint, error):
        print(endpoint, "raised", error)


intents = discord.Intents.all()

client = Client(
    command_prefix=get_prefix,
    case_insensitive=True,
    intents=intents)

client.remove_command('help')

for file in listdir('./Events'):
    if file.endswith('.py'):
        client.load_extension(f'Events.{file[:-3]}')

for file in listdir('./Commands'):
    if file.endswith('.py'):
        client.load_extension(f'Commands.{file[:-3]}')

for file in listdir('./SlashCommands'):
    if file.endswith('.py'):
        client.load_extension(f'SlashCommands.{file[:-3]}')

@client.ipc.route()
async def get_guild_count(data):
    return len(client.guilds)

client.ipc.start()
client.run('')
