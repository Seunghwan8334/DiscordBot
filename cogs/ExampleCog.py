from discord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(name="test")
    @commands.is_owner()
    async def test_cog(self, ctx):
        
        message = "정상 작동 중"

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(ExampleCog(bot))