import discord 
from discord.ext import commands
from configs import discordServerLink

class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @discord.app_commands.command(name="invite")
    async def invite_link(self, interaction: discord.Interaction):
        await interaction.response.send_message(discordServerLink)
    
    @discord.app_commands.command(name="sourcecode")
    async def sourcecode(self, interaction: discord.Interaction):
        await interaction.response.send_message("<https://github.com/Seunghwan8334/DiscordBot>")

async def setup(bot):
    await bot.add_cog(UserCommands(bot))