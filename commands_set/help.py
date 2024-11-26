from initializations import bot

@bot.command(name="help")
async def custom_user_help(ctx):
    help_message = """
### __유저 봇 명령어 목록__
- **$test** 
> 봇의 작동 상태를 확인합니다.
- **$명령어이름**
> 명령어 설명
"""
    await ctx.send(help_message)

@bot.command(name="help-a")
async def custom_admin_help(ctx):
    help_message = """
### __관리자 봇 명령어 목록__
### 모든 $help 안의 명령어도 가능합니다. ### 

- **$test** 
> 봇의 작동 상태를 확인합니다.
- **$명령어이름**
> 명령어 설명
"""
    await ctx.send(help_message)