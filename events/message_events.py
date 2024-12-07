from initializations import * 

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