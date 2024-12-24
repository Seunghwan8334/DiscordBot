from discord.ext import commands

class CogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="load")
    @commands.is_owner()
    async def load_cog(self, ctx, cog_path:str):
        try:
            await self.bot.load_extension(cog_path)
            await ctx.send(f"성공적으로 load했습니다.")
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")
    
    @commands.command(name="unload")
    @commands.is_owner()
    async def unload_cog(self, ctx, cog_path:str):
        try:
            await self.bot.unload_extension(cog_path)
            await ctx.send(f"성공적으로 unload했습니다.")
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")
    
    @commands.command(name="reload")
    @commands.is_owner()
    async def reload_cog(self, ctx, cog_path:str):
        try:
            await self.bot.reload_extension(cog_path)
            await ctx.send(f"성공적으로 reload했습니다.")
        except Exception as e:
            await ctx.send(f"오류 발생: {e}")
    
    @commands.command(name="cogs")
    @commands.is_owner()
    async def all_cogs(self, ctx):
        await ctx.send(f"cogs list : {list(self.bot.cogs.keys())}")
    
async def setup(bot):
    await bot.add_cog(CogCommands(bot))