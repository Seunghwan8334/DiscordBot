from configs import bot, TOKEN
from load_all_cogs import load_all_cogs
import commands_set
import role_buttons_select
import scrapper 
import asyncio

async def main():
    await load_all_cogs(bot)
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
        
    role_buttons_select.button_initialize()

if __name__ == "__main__":
    asyncio.run(main())