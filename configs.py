import discord
from discord.ext import commands

import os 
from dotenv import load_dotenv 
load_dotenv() 

discordServerLink = os.getenv("DISCORD_SERVER_LINK")
bot_token = os.getenv("DISCORD_BOT_TOKEN") 


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.guilds = True 

bot = commands.Bot(command_prefix='$', intents=intents)
bot.help_command = None

TOKEN = bot_token

GUILD_ID = 1286991310657683569

SL_C = SERVERLOG_CHANNEL_ID = 1308733458927063140 
WC_C = WELCOME_CHANNEL_ID =  1304412189725167656 
ST_R = STANDARD_ROLE_ID = 1304313150757273644
ST_C = STANDARD_CHANNEL_ID = 1286991311127187468 

