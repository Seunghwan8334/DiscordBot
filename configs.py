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