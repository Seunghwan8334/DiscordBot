from initializations import *

button_infos = [
    {"label" : "재학생", "role_id" : 1304433147374731266,},
    {"label" : "휴학생", "role_id" : 1304433220875587735,},
    {"label" : "졸업생", "role_id" : 1304433259672764436,},
]

@bot.command(name="create_student_status")
@commands.is_owner() 
async def create_student_status(ctx):
    view = discord.ui.View()

    for i, info in enumerate(button_infos):
        button_infos[i]["custom_id"] = f"button{i+1}"
        button = discord.ui.Button(label=info["label"],style=discord.ButtonStyle.primary, custom_id=info["custom_id"])
        view.add_item(button)

    await ctx.send("버튼을 클릭하면 해당 역할을 부여합니다!", view=view)

@bot.event
async def on_interaction(interaction: discord.Interaction):
    for info in button_infos:
        if (interaction.data.get("custom_id") == info["custom_id"]):
            user = interaction.user
            role = interaction.guild.get_role(info["role_id"])
            
            current_role = None 
            for button_info in button_infos:
                r = interaction.guild.get_role(button_info["role_id"])
                if r in user.roles:
                    current_role = r

            if current_role:
                if current_role == role:
                    await user.remove_roles(role)
                    await interaction.response.send_message(f"{role.mention}역할을 제거하였습니다!", ephemeral=True) 
                else:
                    await user.remove_roles(current_role)
                    await user.add_roles(role) 
                    await interaction.response.send_message(f"{current_role.mention}역할을 제거하고 {role.mention}역할을 부여하였습니다!", ephemeral=True)
            else:
                await user.add_roles(role) 
                await interaction.response.send_message(f"{role.mention}역할을 부여하였습니다!", ephemeral=True) 


            