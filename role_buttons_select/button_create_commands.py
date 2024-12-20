from configs import *
from Database import student_numbers, student_statuses, student_majors, student_genders

@bot.command(name="create_student_number")
@commands.is_owner() 
async def create_student_number(ctx):
    view = discord.ui.View()

    for i, info in enumerate(student_numbers):
        button = discord.ui.Button(
            label=info["label"],
            style=discord.ButtonStyle.primary, 
            custom_id=info["custom_id"]
        )
        view.add_item(button)


    embed = discord.Embed(
        title="아래 버튼을 클릭해주세요!", 
        description="- 버튼을 클릭하면 해당 역할을 부여합니다.", 
        color=0x00bfff
    )
    
    await ctx.send(embed=embed)
    await ctx.send(view=view)


@bot.command(name="create_student_status")
@commands.is_owner() 
async def create_student_status(ctx):
    view = discord.ui.View()

    for i, info in enumerate(student_statuses):
        button = discord.ui.Button(
            label=info["label"], 
            style=discord.ButtonStyle.primary, 
            custom_id=info["custom_id"]
        )
        view.add_item(button)

    embed = discord.Embed(
        title="아래 버튼을 클릭해주세요!", 
        description="- 버튼을 클릭하면 해당 역할을 부여합니다.", 
        color=0x00bfff
    )
    
    await ctx.send(embed=embed)
    await ctx.send(view=view)


@bot.command(name="create_student_major")
@commands.is_owner() 
async def create_student_major(ctx):
    view = discord.ui.View()

    for i, info in enumerate(student_majors):
        button = discord.ui.Button(
            label=info["label"], 
            style=discord.ButtonStyle.primary, 
            custom_id=info["custom_id"]
        )
        view.add_item(button)

    embed = discord.Embed(
        title="아래 버튼을 클릭해주세요!", 
        description="- 버튼을 클릭하면 해당 역할을 부여합니다.", 
        color=0x00bfff
    )
    
    await ctx.send(embed=embed)
    await ctx.send(view=view)

@bot.command(name="create_student_gender")
@commands.is_owner()
async def create_stduent_gender(ctx):
    view = discord.ui.View()
    
    for i, info in enumerate(student_genders):
        button = discord.ui.Button(
            label=info["label"],
            style=discord.ButtonStyle.primary,
            custom_id=info["custom_id"],
            emoji=info["emoji"],
        )
        view.add_item(button)

    embed = discord.Embed(
        title="아래 버튼을 클릭해주세요!", 
        description="- 버튼을 클릭하면 해당 역할을 부여합니다.", 
        color=0x00bfff
    )

    await ctx.send(embed=embed)
    await ctx.send(view=view)
