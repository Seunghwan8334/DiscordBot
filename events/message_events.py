from discord.ext import commands
from datetime import datetime

class MessageEvents(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content} {datetime.now()}")
        if message.author == self.bot.user:
            return
        
async def setup(bot):
    await bot.add_cog(MessageEvents(bot))


