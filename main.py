from configs import bot, TOKEN
from cogs.load_all_cogs import load_all_cogs
import commands
import role_buttons_select
import scrapper 

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

    await load_all_cogs(bot)
    await bot.tree.sync()

    print("Loading all guild data...")
    GuildDataLoader = bot.get_cog("GuildDataLoader")
    GuildDataLoader.load_all_guild_database()
        
    role_buttons_select.button_initialize()

    print("모든 준비 끝!")

if __name__ == "__main__":
    bot.run(TOKEN)