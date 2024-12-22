from configs import *
from Database import student_numbers, student_statuses, student_majors, student_genders
from role_buttons_select.message_generator import generate_message

@bot.event
async def on_interaction(interaction: discord.Interaction):
    user = interaction.user
    #최적화 필요함 귀찮아서 일단 미룸
    for info in student_numbers:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_numbers)

            embed = interaction.message.embeds[0]
            embed.description = generate_message(interaction.guild, student_numbers)
            
            await interaction.message.edit(embed=embed)
            return

    for info in student_statuses:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_statuses)

            embed = interaction.message.embeds[0]
            embed.description = generate_message(interaction.guild, student_statuses)

            await interaction.message.edit(embed=embed)
            return
    
    for info in student_majors:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_majors)

            embed = interaction.message.embeds[0]
            embed.description = generate_message(interaction.guild, student_majors)

            await interaction.message.edit(embed=embed)
            return
    
    for info in student_genders:
        if interaction.data.get("custom_id") == info.get("custom_id"):
            role = interaction.guild.get_role(info["role_id"])
            await toggle_role(interaction, user, role, student_genders)

            embed = interaction.message.embeds[0]
            embed.description = generate_message(interaction.guild, student_genders)

            await interaction.message.edit(embed=embed)
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
                f"{current_role.mention} 역할을 제거하고 {role.mention} 역할을 부여하였습니다!", ephemeral=True)
    else:
        await user.add_roles(role)
        await interaction.response.send_message(f"{role.mention} 역할을 부여하였습니다!", ephemeral=True)

