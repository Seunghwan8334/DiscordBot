from discord.ext import commands

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.database_channel_id = 1322804452457185393
        self.database = {}
    
    async def read_database(self):
        database_channel = self.bot.get_channel(self.database_channel_id)
        async for message in database_channel.history(limit=10): #너무 많은 메세지가 있을 수도 있으니 10개까지만 확인
            if message.content.split('\n')[0] == "discord_user_id":
                pass

        print(f"There's total of {len(self.database)} tables in database")

async def setup(bot):
    await bot.add_cog(Database(bot))    