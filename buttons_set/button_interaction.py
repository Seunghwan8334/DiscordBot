from initializations import *
from .button_data import student_numbers, student_statuses, student_majors

@bot.event
async def on_interaction(interaction: discord.Interaction):
    user = interaction.user

    for info in student_numbers:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_numbers)
            return

    for info in student_statuses:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_statuses)
            return
    
    for info in student_majors:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_majors)
            return

async def toggle_role(interaction, user, role, button_info_group):
    current_role = None
    for info in button_info_group:
        r = interaction.guild.get_role(info["role_id"])
        if r in user.roles:
            current_role = r

    if current_role:
        if current_role == role:
            await user.remove_roles(role)
            await interaction.response.send_message(f"{role.mention} 역할을 제거하였습니다!", ephemeral=True)
        else:
            await user.remove_roles(current_role)
            await user.add_roles(role)
            await interaction.response.send_message(
                f"{current_role.mention} 역할을 제거하고 {role.mention} 역할을 부여하였습니다!", ephemeral=True
            )
    else:
        await user.add_roles(role)
        await interaction.response.send_message(f"{role.mention} 역할을 부여하였습니다!", ephemeral=True)

