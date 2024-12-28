from configs import bot, TOKEN
from cogs.load_all_cogs import load_all_cogs

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")

    await load_all_cogs(bot)
    await bot.tree.sync()

    GuildDataLoader = bot.get_cog("GuildDataLoader")
    GuildDataLoader.load_all_guild_database()

    print("Bot ready to use!")

if __name__ == "__main__":
    bot.run(TOKEN)