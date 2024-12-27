from configs import *
from Database import student_numbers, student_statuses, student_majors, student_genders
from role_buttons_select.message_generator import generate_message

@bot.event
async def on_interaction(interaction: discord.Interaction):
    user = interaction.user
    custom_id = interaction.data.get("custom_id")
    if "student" in custom_id:
        if "number" in custom_id:
            for info in student_numbers:
                if custom_id == info.get("custom_id"):
                    role = interaction.guild.get_role(info["role_id"])
                    await toggle_role(interaction, user, role, student_numbers)
                    await update_message(interaction, student_numbers)
                    return
        elif "status" in custom_id:
            for info in student_statuses:
                if custom_id == info.get("custom_id"):
                    role = interaction.guild.get_role(info["role_id"])
                    await toggle_role(interaction, user, role, student_statuses)
                    await update_message(interaction, student_statuses)
                    return
        elif "major" in custom_id:
            for info in student_majors:
                if custom_id == info.get("custom_id"):
                    role = interaction.guild.get_role(info["role_id"])
                    await toggle_role(interaction, user, role, student_majors)
                    await update_message(interaction, student_majors)
                    return
        elif "gender" in custom_id:
            for info in student_genders:
                if custom_id == info.get("custom_id"):
                    role = interaction.guild.get_role(info["role_id"])
                    await toggle_role(interaction, user, role, student_genders)
                    await update_message(interaction, student_genders)
                    return
        else:
            print("student 존재하지 않는 custom_id 입니다.")
    elif "hufs" in custom_id:
        role_id = int(custom_id[0:19])
        role = interaction.guild.get_role(role_id)
        if role in user.roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"{role.mention} 역할을 제거하였습니다!", ephemeral=True)
        else:
            await user.add_roles(role)
            await interaction.response.send_message(f"{role.mention} 역할을 부여하였습니다!", ephemeral=True)
    else:
        print("존재하지 않는 custom_id 입니다.")

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
                f"{current_role.mention} 역할을 제거하고 {role.mention} 역할을 부여하였습니다!", ephemeral=True)
    else:
        await user.add_roles(role)
        await interaction.response.send_message(f"{role.mention} 역할을 부여하였습니다!", ephemeral=True)

async def update_message(interaction, button_info_group):
    embed = interaction.message.embeds[0]
    embed.description = generate_message(interaction.guild, button_info_group)
            
    await interaction.message.edit(embed=embed)

