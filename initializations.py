import discord
from discord.ext import commands
from secret_file import bot_token

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.guilds = True 

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = bot_token

GUILD_IDS = [
    1286991310657683569,
]

SCI = 1308733458927063140 #SERVERLOG_CHANNEL_ID
