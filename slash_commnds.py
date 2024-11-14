from initializations import *

@bot.tree.command(name="hello", description="Say Hello", guild=GUILD)
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello there")

@bot.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@bot.tree.command(name="test", description="This is a slash test command!", guild=GUILD) 
async def slash_test(interaction: discord.Interaction):
    await interaction.response.send_message("This is a slash test command!") 