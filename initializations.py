import discord
from discord.ext import commands
import os 
from dotenv import load_dotenv 
load_dotenv() 
bot_token = os.getenv("DISCORD_BOT_TOKEN") 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.guilds = True 

bot = commands.Bot(command_prefix='$', intents=intents)
bot.help_command = None

TOKEN = bot_token

GUILD_IDS = [
    1286991310657683569,
]

SL_C = 1308733458927063140 # SERVERLOG_CHANNEL_ID
WC_C = 1304412189725167656 # WELCOME_CHANNEL_ID
ST_R = 1304313150757273644 # STANDARD_ROLE_ID
ST_C = 1286991311127187468 # STANDARD_CHANNEL_ID

