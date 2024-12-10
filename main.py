from configs import bot, TOKEN
from events.message_events import *
import commands_set
import buttons_set
import scrapper 
import asyncio

async def main():
    await bot.load_extension("events.member_events")
    await bot.load_extension("events.command_errors")
    #await bot.load_extension("events.message_events")
    await bot.load_extension("guildDataLoad")
    await bot.start(TOKEN)

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

    print("Loading all guild data...")
    GuildDataLoader = bot.get_cog("GuildDataLoader")
    if GuildDataLoader:
        GuildDataLoader.load_all_guild_database() 
    else:
        print("GuildDataLoader not found")
        
    buttons_set.button_initialize()

if __name__ == "__main__":
    asyncio.run(main())