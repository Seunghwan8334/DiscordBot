from configs import bot, TOKEN
from cogs.load_all_cogs import load_all_cogs

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

    GuildDataLoader = bot.get_cog("GuildDataLoader")
    GuildDataLoader.load_all_guild_database()

    print("Bot ready to use!")

@bot.event
async def setup_hook():
    await load_all_cogs(bot)
    await bot.tree.sync()


if __name__ == "__main__":
    bot.run(TOKEN)