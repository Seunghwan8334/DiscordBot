from initializations import *

#bot = commands.Bot(command_prefix='$', intents=intents)

bot.help_command = None

@bot.command(name="help")
async def custom_help(ctx):
    help_message = """
### __사용 가능한 봇 명령어 목록__
- **$test** 
> 봇의 작동 상태를 확인합니다.
- **$명령어이름**
> 명령어 설명
"""
    await ctx.send(help_message)

@bot.command(name="test") 
async def test(ctx):
    await ctx.send("정상 가동 중..")

@bot.command(name="server")
async def server(ctx):
    await ctx.send(ctx.guild)

@bot.command(name="add") #Basic converter
async def add(ctx, a: int,b: int):
    await ctx.send(a+b)



