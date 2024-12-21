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
        

        if message.content.startswith("봇아"):
            if message.author == message.guild.owner:
                await message.channel.send(f"예 행님")
            else:
                await message.channel.send(f"이 명령어는 서버 주인만 사용할 수 있어요.")
        
        #await self.bot.process_commands(message)
        
async def setup(bot):
    await bot.add_cog(MessageEvents(bot))


