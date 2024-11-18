import discord
from discord.ext import commands
from secret_file import bot_token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

TOKEN = bot_token

GUILD_IDS = [
    1286991310657683569,
    933332325582909480,
]
