cogs = [
    "student_role_select.button_create_commands",
    "student_role_select.button_interaction",

    "events.member_events",
    "events.command_errors",
    "events.message_events",

    "guildDataLoad",
    
    "commands.user_commands",
    "commands.admin_commands",

    "cogs.cog_commands",
    "cogs.example_cog",

    "hufs.hufs_alarm",
    "hufs.hufs_commands",
    "hufs.hufs_messages", #hufs_monitor에서 hufs_message를 사용함. 혹시 오류 주의
    "hufs.hufs_monitor",
]

async def load_all_cogs(bot):

    for cog in cogs:
        try:
            await bot.load_extension(cog)
        except Exception as e:
            print(f"{cog}를 로드하는 것을 실패하였습니다. 오류: {e}")
