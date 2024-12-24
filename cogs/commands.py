# from discord.ext import commands

# class CogCommands(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot 
    
#     @commands.command(name="add_cog")
#     @commands.is_owner()
#     async def add_cog(self, ctx, cog):
#         await self.bot.add_cog(cog) 
    
#     @commands.command(name="remove_cog")
#     @commands.is_owner()
#     async def remove_cog(self, ctx, cog):
#         await self.bot.remove_cog(cog)

#     @commands.command(name="load_cog")
#     @commands.is_owner()
#     async def load_cog(self, ctx, cog_path:str):
#         await self.bot.load_extension(cog_path)
    
#     @commands.command(name="unload_cog")
#     @commands.is_owner()
#     async def unload_cog(self, ctx, cog_path:str):
#         await self.bot.unload_extension(cog_path)
    
#     @commands.command(name="reload_cog")
#     @commands.is_owner()
#     async def reload_cog(self, ctx, cog_path:str):
#         await self.bot.reload_extension(cog_path)
    
#     @commands.command(name="cogs")
#     @commands.is_owner()
#     async def all_cogs(self, ctx):
#         await ctx.send(f"cogs list : {list(self.bot.cogs.keys())}")
    
# async def setup(bot):
#     await bot.add_cog(CogCommands(bot))