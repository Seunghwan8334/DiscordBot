from initializations import * #초기 변수 선언 파일
from welcome import *
from slash_commnds import * #slash 명령어 파일
from user_prefix_commands import * #user 명령어 파일
from admin_prefix_commands import * #admin 명령어 파일
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
            print(f"{GUILD.name} ({GUILD_ID})와 연결 성공")
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
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'You reacted {reaction}!')

@bot.listen("on_reaction_add") #이거 왜 on_reaction_add만 안 될까 
async def my_message(reaction, user): #해결 완료
    print(f"reaction detected!")

bot.run(TOKEN)
