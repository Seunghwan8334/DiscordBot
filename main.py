from initializations import *
import commands_set
from message_events import * 
from member_events import *
from embeds import *
from command_errors import *
import scrapper 

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
    
    if message.content.startswith("봇아"):
        if message.author == message.guild.owner:
            await message.channel.send(f"예 행님")
        else:
            await message.channel.send(f"이 명령어는 서버 주인만 사용할 수 있어요.")

    await bot.process_commands(message) #이 문장이 없으니 prefix 명령어가 감지 되지 않았음

@bot.event
async def on_reaction_add(reaction, user):
    #await reaction.message.channel.send(f'You reacted {reaction}!')
    pass

@bot.listen("on_reaction_add") 
async def my_message(reaction, user):
    pass

bot.run(TOKEN)
