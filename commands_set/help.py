from initializations import *

@bot.command(name="help")
async def custom_user_help(ctx):
    help_message = """
### __유저 봇 명령어 목록__
[]: 필수 {}: 선택

- **$test** 
> 봇의 작동 상태를 확인합니다.
- **$profile {유저}**
> 유저를 입력하면 해당 유저 정보를 보여줍니다. 입력하지 않으면 자신의 정보를 출력합니다.
- **$invite**
> 디스코드 서버의 초대 링크를 출력합니다.
- **$code**
> 봇의 소스코드를 공유합니다.
- **$add [정수1] [정수2]**
> [정수1]과 [정수2]를 합한 값을 출력합니다.
"""
    await ctx.send(help_message)

@bot.command(name="help-a")
@commands.has_permissions(administrator=True)
async def custom_admin_help(ctx):
    help_message = """
### __관리자 봇 명령어 목록__
### 모든 $help 안의 명령어도 가능합니다. ### 
[]: 필수 {}: 선택

- **$say [채널] [내용]**
> [채널]에 봇이[내용]을 출력합니다.
- **$clear [정수]**
> $clear 명령어를 제외한 위 채팅 내용의 [정수]개를 삭제합니다. 
- **$kick [유저] {내용}**
> 해당 [유저]를 추방하고 해당 채널에 {내용:사유}를 출력합니다.
- **$ban [유저] {내용}**
> 해당 [유저]를 밴하고 해당 채널에 {내용:사유}를 출력합니다.
- **$shutdown**
> 봇을 비활성화합니다.
- **$sync**
> 봇의 모든 슬레시 명령어를 동기화합니다.
- **$명령어이름**
> 명령어 설명

"""
    await ctx.send(help_message)