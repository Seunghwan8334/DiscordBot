from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup
from .hufs_database import *
import asyncio
from datetime import datetime
import pytz

class HufsMonitor(commands.Cog):
    def __init__(self ,bot):
        self.bot = bot 
        self.monitor_status = False
        self.monitor_message = None
        self.task = None

        self.increment1 = HUFS_INCREMENT1
        self.increment2 = HUFS_INCREMENT2
        self.increment3 = HUFS_INCREMENT3

        self.status1 = None #한국외대 -공지(웹사이트)- 연결 상태
        self.status2 = None #한국외대 -학사(웹사이트)- 연결 상태
        self.status3 = None #한국외대 -장학(웹사이트)- 연결 상태

        self.channel1_status = None #디스코드 -공지(채널)- 연결 상태
        self.channel2_status = None #디스코드 -학사(채널)- 연결 상태
        self.channel3_status = None #디스코드 -장학(채널)- 연결 상태

        self.role1_status = None #디스코드 -공지(역할)- 연결 상태
        self.role2_status = None #디스코드 -학사(역할)- 연결 상태
        self.role3_status = None #디스코드 -장학(역할)- 연결 상태

        self.last_update = None #마지막으로 업데이트한 시간
        self.monitor_cycle = 300 #monitor 주기
        self.message = bot.get_cog("HufsMessages").monitor_message
        self.message_for_channel = bot.get_cog("HufsMessages").channel_message

    @commands.command(name="monitor_on")
    @commands.is_owner()
    async def monitor_on(self, ctx):
        if self.monitor_status is True:
            await ctx.send("monitor is already ON")
        else:
            await ctx.send("turning ON monitor..") 
            message = self.message.format(
                self.status1, self.status2, self.status3, 
                self.channel1_status, self.channel2_status, self.channel3_status,
                self.role1_status, self.role2_status, self.role3_status,                
                self.last_update, self.monitor_cycle)
            self.monitor_message = await ctx.send(message)
            self.monitor_status = True
            self.task = asyncio.create_task(self.loop(ctx))
    
    @commands.command(name="monitor_off")
    @commands.is_owner()
    async def monitor_off(self, ctx):
        if self.monitor_status is False:
            await ctx.send("monitor is already OFF")
        else:
            await ctx.send("turning OFF monitor..")
            try:
                await self.monitor_message.delete()
                self.monitor_message = None 
            except Exception as e:
                print(f"메시지 삭제 중 오류 발생: {e}")
            
            self.monitor_status = False

            if self.task:
                try:
                    self.task.cancel()
                except Exception as e:
                    print(f"작업 취소 중 오류 발생: {e}")
    
    async def check_url(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:  # 비동기적으로 응답 받기
                status = response.status
                html = await response.text()
                return status, html
    
    def get_list(self, soup):
        body = soup.find("tbody")
        td_list = body.find_all("tr")
        new_list = []

        for td in td_list:
            td_num = td.find("td",class_="td-num").text.strip()
            td_subject = td.find("td",class_="td-subject").find("a").find("strong").text.strip()
            td_write = td.find("td",class_="td-write").text.strip()
            td_date = td.find("td",class_="td-date").text.strip()
            td_link = td.find("td",class_="td-subject").find("a")["href"]
            if td_num.isdigit() == False:
                continue
            new_list.append({"number":int(td_num), "subject":td_subject, "writer":td_write, "date":td_date, "link":"<https://www.hufs.ac.kr"+td_link+">"})
        
        return new_list

    
    async def loop(self, ctx):
        while self.monitor_status:

            role1 = ctx.guild.get_role(HUFS_ROLE1_ID)
            role2 = ctx.guild.get_role(HUFS_ROLE2_ID)
            role3 = ctx.guild.get_role(HUFS_ROLE3_ID)

            if role1 is not None: self.role1_status = "🟢"
            else: self.role1_status = "❌"
            if role2 is not None: self.role2_status = "🟢"
            else: self.role2_status = "❌"
            if role3 is not None: self.role3_status = "🟢"
            else: self.role3_status = "❌"

            channel1 = ctx.guild.get_channel(HUFS_CHANNEL1_ID)
            channel2 = ctx.guild.get_channel(HUFS_CHANNEL2_ID)
            channel3 = ctx.guild.get_channel(HUFS_CHANNEL3_ID)

            if channel1 is not None: self.channel1_status = "🟢"
            else: self.channel1_status = "❌"
            if channel2 is not None: self.channel2_status = "🟢"
            else: self.channel2_status = "❌"
            if channel3 is not None: self.channel3_status = "🟢"
            else: self.channel3_status = "❌"



            response1_status, html1 = await self.check_url(HUFS_LINK1)
            response2_status, html2 = await self.check_url(HUFS_LINK2)
            response3_status, html3 = await self.check_url(HUFS_LINK3)

            if response1_status == 200:
                self.status1 = "🟢"
                soup = BeautifulSoup(html1, 'html.parser')
                new_list1 = self.get_list(soup)
                for info in new_list1[::-1]:
                    if info["number"] > self.increment1:
                        self.increment1 = info["number"]
                        await channel1.send(self.message_for_channel.format(
                            info["subject"], info["number"], info["writer"], info["date"], info["link"], role1.mention
                        ))
            else: self.status1 = "❌"

            if response2_status == 200:
                self.status2 = "🟢"
                soup = BeautifulSoup(html2, 'html.parser')
                new_list2 = self.get_list(soup)
                for info in new_list2[::-1]:
                    if info["number"] > self.increment2:
                        self.increment2 = info["number"]
                        await channel2.send(self.message_for_channel.format(
                            info["subject"], info["number"], info["writer"], info["date"], info["link"], role2.mention
                        ))
                
            else: self.status2 = "❌"

            if response3_status == 200:
                self.status3 = "🟢"
                soup = BeautifulSoup(html3, 'html.parser')
                new_list3 = self.get_list(soup)
                for info in new_list3[::-1]:
                    if info["number"] > self.increment3:
                        self.increment3 = info["number"]
                        await channel3.send(self.message_for_channel.format(
                            info["subject"], info["number"], info["writer"], info["date"], info["link"], role3.mention
                        ))
                
            else: self.status3 = "❌"
            
            kst = pytz.timezone('Asia/Seoul')
            self.last_update = datetime.now(kst).strftime("%Y년 %m월 %d일 - %H시 %M분 %S초")
            message = self.message.format(
                self.status1, self.status2, self.status3, 
                self.channel1_status, self.channel2_status, self.channel3_status,
                self.role1_status, self.role2_status, self.role3_status,
                self.last_update, self.monitor_cycle
            )

            await self.monitor_message.edit(content=message)
            await asyncio.sleep(self.monitor_cycle)
    


async def setup(bot):
    await bot.add_cog(HufsMonitor(bot))

