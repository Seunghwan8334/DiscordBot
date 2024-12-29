from discord.ext import commands

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.database_channel_id = 1322804452457185393
        self.database = {
            "solvedac" : {
                "discord_user_id" : [],
                "baekjoon_user_name" : [],
            },
            "hufs" : {
                "increments" : []
            }
        }

async def setup(bot):
    await bot.add_cog(Database(bot))