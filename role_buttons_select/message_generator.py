
def generate_message(guild, role_info_list):
    message = f"**버튼을 클릭하면 해당 역할을 부여합니다.**\n"
    notSelected = len(guild.members)
    for role_info in role_info_list:
        role_name = role_info["label"]
        role_id = role_info["role_id"]
        role = guild.get_role(role_id)
        if role:
            member_count = len(role.members)
            message += f"- {role_name}: {member_count}명\n"
            notSelected -= member_count
        else:
            message += f"{role_name}: Error명\n"
    message += f"선택 안함: {notSelected}명\n"

    return message 