from discord.ext import commands
import discord

class Interaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        custom_id = interaction.data.get("custom_id")
        if "student" in custom_id:
            await self.bot.get_cog("StudentButtonInteraction").interaction(interaction)
        elif "hufs" in custom_id:
            await self.bot.get_cog("HufsButtonInteraction").interaction(interaction)
        else:
            print("there must be an error.")

async def setup(bot):
    await bot.add_cog(Interaction(bot))