from discord.ext import commands
import aiohttp
from .hufs_database import *

class HufsCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    async def check_url_status(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:  # 비동기적으로 응답 받기
                return response.status
    
    @commands.command(name="check_hufs_connect")
    @commands.is_owner()
    async def check_hufs_connect(self, ctx):

        if ctx.guild.get_channel(HUFS_CHANNEL1_ID): await ctx.send("한국외대 -공지(채널)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -공지(채널)- ❌ 연결상태: 문제 발생")
        if ctx.guild.get_channel(HUFS_CHANNEL2_ID): await ctx.send("한국외대 -학사(채널)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -학사(채널)- ❌ 연결상태: 문제 발생")
        if ctx.guild.get_channel(HUFS_CHANNEL3_ID): await ctx.send("한국외대 -장학(채널)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -장학(채널)- ❌ 연결상태: 문제 발생")

        response1 = await self.check_url_status(HUFS_LINK1)
        if response1 == 200: await ctx.send("한국외대 -공지(웹사이트)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -공지(웹사이트)- ❌ 연결상태: 문제 발생")
        response2 = await self.check_url_status(HUFS_LINK2)
        if response2 == 200: await ctx.send("한국외대 -학사(웹사이트)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -학사(웹사이트)- ❌ 연결상태: 문제 발생")
        response3 = await self.check_url_status(HUFS_LINK3)
        if response3 == 200: await ctx.send("한국외대 -장학(웹사이트)- 🟢 연결상태: 정상")
        else: await ctx.send("한국외대 -장학(웹사이트)- ❌ 연결상태: 문제 발생")

        await ctx.send("검사 끝.")

    @commands.command(name="set_data")
    @commands.has_permissions(administrator=True)
    async def set_data(self, ctx, ar1, ar2, ar3):
        HufsMonitor = self.bot.get_cog("HufsMonitor")
        HufsMonitor.increment1 = ar1 
        HufsMonitor.increment2 = ar2 
        HufsMonitor.increment3 = ar3
        await ctx.send(f"data set to : {ar1, ar2, ar3}")
    
    @commands.command(name="get_data")
    @commands.has_permissions(administrator=True)
    async def get_data(self, ctx):
        HufsMonitor = self.bot.get_cog("HufsMonitor")
        ar1 = HufsMonitor.increment1 
        ar2 = HufsMonitor.increment2 
        ar3 = HufsMonitor.increment3 
        await ctx.send(f"datas are {ar1}, {ar2}, {ar3}")

async def setup(bot):
    await bot.add_cog(HufsCommands(bot))