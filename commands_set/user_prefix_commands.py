from configs import *

@bot.command(name="invite") 
async def invite_link(ctx):
    await ctx.send(discordServerLink)

@bot.command(name="profile")
async def send_embed(ctx, member:discord.Member = None):
    if member:
        user = member
    else: 
        user = ctx.author

    embed = discord.Embed(
        title=f"{user.name}'s profile",
        description="This is the description of your profile",
        color=discord.Color.blue()
    )

    embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Nickname", value=user.display_name, inline=True)
    embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
    embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S") if user.joined_at else "N/A", inline=False)
    embed.set_footer(text="Your Discord Profile")

    await ctx.send(embed=embed)

@bot.command(name="sourcecode") 
async def sourcecode(ctx):
    await ctx.send("<https://github.com/Seunghwan8334/DiscordBot>")



