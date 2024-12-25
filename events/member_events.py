from discord.ext import commands

class MemberEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        GuildDataLoader = self.bot.get_cog("GuildDataLoader")

        welcome_channel = GuildDataLoader.guildInfo[member.guild.id].welcome_channel
        serverlog_channel = GuildDataLoader.guildInfo[member.guild.id].serverlog_channel
        standard_role = GuildDataLoader.guildInfo[member.guild.id].standard_role

        if welcome_channel:
            await welcome_channel.send(f"안녕하세요 {member.mention}님! {member.guild.name}에 오신 것을 환영합니다!!^^")
            await serverlog_channel.send(f"{member.mention}님이 서버에 들어오셨어요.")
        else:
            await serverlog_channel.send(f"{member.mention}님의 환영인사를 보낼 채널을 찾지 못했어요.")
        
        if standard_role:
            await member.add_roles(standard_role)
        else:
            await serverlog_channel.send(f"{member.mention}님에게 {standard_role.mention}을 부여하는 것을 실패하였습니다.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        GuildDataLoader = self.bot.get_cog("GuildDataLoader")

        serverlog_channel = self.bot.get_channel(GuildDataLoader.guildInfo[member.guild.id].serverlog_channel.id)
        if serverlog_channel:
            await serverlog_channel.send(f"{member.mention}님이 서버를 나가셨어요.")

async def setup(bot):
    await bot.add_cog(MemberEvents(bot))