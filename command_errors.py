from initializations import bot, commands

@bot.event 
async def on_command_error(ctx,error): #명령어 오류 감지
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자 권한이 필요한 명령어 입니다") 
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("이런 명령어는 없는데. 오타라도 내셨나요?")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("명령어 뒤에 (args)을 추가해 주세요")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("해당 유저는 존재하지 않습니다.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("해당 명령어는 봇 소유자만 사용 가능합니다.")
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send("해당 채널은 존재하지 않습니다.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("봇의 권한이 부족합니다.")
    else:
        await ctx.send(f"으잉? 이런 명령어 오류는 예상 못 했는데.. {ctx.guild.owner.mention} 야 이것 좀 고쳐봐")