from initializations import * #초기 변수 선언 파일
from slash_commnds import * #slash 명령어 파일
from prefix_commands import * #prefix 명령어 파일
import scrapper #solved ac 웹사이트 scrapper

@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")
    
    if scrapper.STATUS_CODE == 200:
        print(f"solved.ac 연결 성공")
    else:
        print(f"solved.ac 연결 문제발생")

    print(f"모든 디스코드 서버 연결 중..")
    for GUILD_ID in GUILD_IDS:
        GUILD = bot.get_guild(GUILD_ID)
        if GUILD:
            print(f"{GUILD.name} 와 연결 성공")
        else:
            print(f"존재하지 않는 서버입니다")

@bot.event
async def on_message(message):
    print(f"Message from {message.author}: {message.content}")
    if message.author == bot.user:  #무한반복 방지
        return
    
    if message.content.startswith("hello"):
        await message.channel.send(f"Hi there {message.author}")

    await bot.process_commands(message) #이 문장이 없으니 prefix 명령어가 감지 되지 않았음

@bot.event 
async def on_command_error(ctx,error): #명령어 오류 감지
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자 권한이 필요한 명령어 입니다") 
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("이런 명령어는 없는데. 오타라도 내셨나요?")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("명령어 뒤에 (arg1)을 추가해 주세요")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("해당 유저는 존재하지 않습니다.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("해당 명령어는 봇 소유자만 사용 가능합니다.")
    else:
        await ctx.send("으잉? 이런 명령어 오류는 예상 못 했는데.. 봇 제작자에게 문의해봐요")

@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'You reacted {reaction}!')

@bot.listen("on_reaction_add") #이거 왜 on_reaction_add만 안 될까 
async def my_message(reaction, user): #해결 완료
    print(f"reaction detected!")

bot.run(TOKEN)
