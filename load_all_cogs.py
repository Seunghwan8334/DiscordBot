from discord.ext import commands

cogs = [
    "commands_set.help_prefix_commands",
    "events.member_events",
    "events.command_errors",
    "events.message_events",
    "guildDataLoad"
]

async def load_all_cogs(bot):

    for cog in cogs:
        try:
            await bot.load_extension(cog)
            print(f"{cog}가 로드되었습니다.")
        except Exception as e:
            print(f"{cog}를 로드하는 것을 실패하였습니다. 오류: {e}")
