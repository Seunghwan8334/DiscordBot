from discord.ext import commands

class GetAlarm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="create_hufs_button")
    @commands.is_owner()
    async def create_hufs_button(self, ctx):
        
        pass
        view = 1
        message = 2
        await ctx.send(message, view=view)
    

