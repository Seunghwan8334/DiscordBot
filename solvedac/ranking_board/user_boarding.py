from discord.ext import commands

class UserBoarding(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="onboard")
    async def onboard(self, ctx, baekjoon_user_name:str):
        pass

    @commands.command(name="offboard")
    async def offboard(self, ctx, baekjoon_user_name:str):
        pass

async def setup(bot):
    await bot.add_cog(UserBoarding(bot))