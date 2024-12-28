from discord.ext import commands
import discord 

class HufsButtonInteraction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    async def interaction(self, interaction: discord.Interaction):
        custom_id = interaction.data.get("custom_id")
        
        user = interaction.user
        role_id = int(custom_id[0:19])
        role = interaction.guild.get_role(role_id)
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"{role.mention} 역할을 제거하였습니다!", ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"{role.mention} 역할을 부여하였습니다!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(HufsButtonInteraction(bot))
        