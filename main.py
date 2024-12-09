from configs import *
import commands_set
import buttons_set
import events
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
    
    buttons_set.button_initialize()

@bot.event
async def on_reaction_add(reaction, user):
    #await reaction.message.channel.send(f'You reacted {reaction}!')
    pass

@bot.listen("on_reaction_add") 
async def my_message(reaction, user):
    pass

bot.run(TOKEN)
