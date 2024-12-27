from discord.ext import commands
import discord
from .hufs_database import HUFS_ROLE1_ID, HUFS_ROLE2_ID, HUFS_ROLE3_ID

class GetAlarm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="create_hufs_button")
    @commands.is_owner()
    async def create_hufs_button(self, ctx):
        view = discord.ui.View()
        
        button1 = discord.ui.Button(label="공지", style=discord.ButtonStyle.primary, custom_id=f"{HUFS_ROLE1_ID}_hufs_1")
        button2 = discord.ui.Button(label="학사", style=discord.ButtonStyle.primary, custom_id=f"{HUFS_ROLE2_ID}_hufs_2")
        button3 = discord.ui.Button(label="장학", style=discord.ButtonStyle.primary, custom_id=f"{HUFS_ROLE3_ID}_hufs_3")
        
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        embed = discord.Embed(
            title="아래 버튼을 클릭해주세요!", 
            description="알림 받고 싶으신 역할 버튼을 눌러주세요", 
            color=0x00bfff
        )

        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(GetAlarm(bot))