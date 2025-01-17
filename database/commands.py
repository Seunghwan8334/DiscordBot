from discord.ext import commands

class DatabaseCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="generate_database")
    @commands.has_permissions(administrator=True)
    async def generate_database(self, ctx):
        database = self.bot.get_cog("Database")

        message = "discord_user_id\n"
        for data in database["solvedac"]["discord_user_id"]:
            message += f"{data}, "
        message += f"\ntotal of {len(database["solvedac"]["discord_user_id"])} datas in this table"
        await ctx.send(message)

        message = "baekjoon_user_name\n"
        for data in database["solvedac"]["baekjoon_user_name"]:
            message += f"{data}, "
        message += f"\ntotal of {len(database["solvedac"]["baekjoon_user_name"])} datas in this table"
        await ctx.send(message)

        message = "increments\n"
        for data in database["hufs"]["increments"]:
            message += f"{data}"
        message += f"\ntotal of {len(database["hufs"]["increments"])} datas in this table"


    @commands.command(name="set_database")
    @commands.has_permissions(administrator=True)
    async def set_database(self):
        database = self.bot.get_cog("Database")

        database_channel = self.bot.get_channel(database.database_channel_id)
        async for message in database_channel.history(limit=10): #너무 많은 메세지가 있을 수도 있으니 10개까지만 확인
            if message.content.split('\n')[0] == "discord_user_id":
                pass

        print(f"There's total of {len(self.database)} tables in database")


async def setup(bot):
    await bot.add_cog(DatabaseCommands(bot))