# @bot.command(name="profile")
# async def send_embed(ctx, member:discord.Member = None):
#     if member:
#         user = member
#     else: 
#         user = ctx.author

#     embed = discord.Embed(
#         title=f"{user.name}'s profile",
#         description="This is the description of your profile",
#         color=discord.Color.blue()
#     )

#     embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
#     embed.add_field(name="ID", value=user.id, inline=True)
#     embed.add_field(name="Nickname", value=user.display_name, inline=True)
#     embed.add_field(name="Account Created", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
#     embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S") if user.joined_at else "N/A", inline=False)
#     embed.set_footer(text="Your Discord Profile")

#     await ctx.send(embed=embed)

# @bot.command(name="kick")
# @commands.has_permissions(kick_members=True)
# async def kick(ctx, member:discord.Member,*,reason=None):
#     try:
#         await member.kick(reason=reason)
#         await ctx.channel.send(f"{member.mention}님이 추방되었습니다.")
#         if reason:
#             await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 추방하였습니다.\n사유: {reason}")
#         else:
#             await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 추방하였습니다.\n사유: 정의되지 않음.")
#     except discord.Forbidden:
#         await ctx.channel.send("권한이 부족하여 해당 멤버를 추방할 수 없습니다.")
#     except Exception as e:
#         await ctx.channel.send(f"예기치 못한 오류가 발생하였습니다.")

# @bot.command(name="ban")
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, member: discord.Member, *, reason=None):
#     try:
#         await member.ban(reason=reason)
#         await ctx.channel.send(f"{member.mention}님이 밴되었습니다.")
#         if reason:
#             await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 밴하였습니다.\n사유: {reason}")
#         else:
#             await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 밴하였습니다.\n사유: 정의되지 않음.")
#     except discord.Forbidden:
#         await ctx.channel.send("권한이 부족하여 해당 멤버를 밴할 수 없습니다.")
#     except Exception as e:
#         await ctx.channel.send(f"예기치 못한 오류가 발생하였습니다.")