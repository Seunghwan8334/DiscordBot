from initializations import bot, SCI

WELCOME_CHANNEL_ID = 1304412189725167656
STANDARD_ROLE_ID = 1304313150757273644

@bot.event
async def on_member_join(member):
    guild = member.guild
    welcome_channel = bot.get_channel(WELCOME_CHANNEL_ID)
    SERVERLOG = bot.get_channel(SCI)
    role = guild.get_role(STANDARD_ROLE_ID)

    if welcome_channel:
        await welcome_channel.send(f"안녕하세요 {member.mention}님! {member.guild.name}에 오신 것을 환영합니다!!^^")
        await SERVERLOG.send(f"{member.mention}님이 서버에 들어오셨어요.")
    else:
        await SERVERLOG.send(f"{member.mention}님의 환영인사를 보낼 채널을 찾지 못했어요.")
    
    if role:
        await member.add_roles(role)
        await SERVERLOG.send(f"{member.mention}님에게 {role.mention}을 부여하였습니다.")
    else:
        await SERVERLOG.send(f"{member.mention}님에게 {role.mention}을 부여하는 것을 실패하였습니다.")

@bot.event 
async def on_member_remove(member):
    SERVERLOG = bot.get_channel(SCI)
    if SERVERLOG:
        await SERVERLOG.send(f"{member.mention}님이 서버를 나가셨어요.")