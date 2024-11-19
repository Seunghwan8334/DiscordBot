from initializations import *

WELCOME_CHANNEL_ID = 1304412189725167656

@bot.event
async def on_member_join(member):
    guild = member.guild
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if welcome_channel:
        await welcome_channel.send(f"안녕하세요 {member.mention}님! {member.guild.name}에 오신 것을 환영합니다!!^^")
    else:
        await bot.get_channel(1308334762838069298).send("환영인사를 보낼 채널을 찾지 못했어요.ㅠㅜ")