from configs import bot, commands, discord, SL_C

@bot.command(name="say")
@commands.has_permissions(administrator=True)
async def say(ctx, *, args):
    if ctx.author == bot.user:
        await ctx.channel.send("무한반복 감지!!")
    try:
        parts = args.split()
        if parts[-1].startswith("<#") and parts[-1].endswith(">"):
            message_content = " ".join(parts[:-1])
            channel_id = int(parts[-1][2:-1])
            target_channel = bot.get_channel(channel_id)

            if target_channel:
                await target_channel.send(message_content)
                await ctx.channel.send(f"메세지를 {target_channel.mention}에 보냈습니다.")
            else:
                await ctx.channel.send(f"해당 채널을 찾을 수 없습니다.")
        else:
            await ctx.channel.send(f"명령어 형식을 따라해주세요.\n$say [메세지] [보낼채널]")  
    except Exception as e:
        await ctx.send(f"오류가 발생했습니다: {e}")

@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num:int):
    if num < 1:
        await ctx.channel.send("1 이상의 숫자를 입력해주세요.") 
    elif num > 20:
        await ctx.channel.send("최대 20개의 메세지까지 지울 수 있습니다.")
    else:
        deleted = await ctx.channel.purge(limit=num+1)
        await ctx.channel.send(f"{len(deleted)-1}개의 메세지를 삭제하였습니다.(2초 후 삭제)",delete_after=2)

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member,*,reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.channel.send(f"{member.mention}님이 추방되었습니다.")
        if reason:
            await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 추방하였습니다.\n사유: {reason}")
        else:
            await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 추방하였습니다.\n사유: 정의되지 않음.")
    except discord.Forbidden:
        await ctx.channel.send("권한이 부족하여 해당 멤버를 추방할 수 없습니다.")
    except Exception as e:
        await ctx.channel.send(f"예기치 못한 오류가 발생하였습니다.")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.channel.send(f"{member.mention}님이 밴되었습니다.")
        if reason:
            await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 밴하였습니다.\n사유: {reason}")
        else:
            await bot.get_channel(SL_C).send(f"{ctx.author.mention}님이 {member.mention}님을 밴하였습니다.\n사유: 정의되지 않음.")
    except discord.Forbidden:
        await ctx.channel.send("권한이 부족하여 해당 멤버를 밴할 수 없습니다.")
    except Exception as e:
        await ctx.channel.send(f"예기치 못한 오류가 발생하였습니다.")


@bot.command(name="shutdown")  
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("shutting down...") 
    await bot.close() 

@bot.command(name="sync", help="sync all slash commands in discord servers")
@commands.is_owner()
async def sync_313(ctx):
    await ctx.send(f"------------------------------------\n슬레시 명령어 동기화 중..")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
        await ctx.send("동기화 성공!")
    except Exception as e:
        print(f"Error syncing commands: {e}")
        await ctx.send("동기화 실패..")

@bot.command(name="cogs")
@commands.is_owner()
async def cogs(ctx):
    await ctx.send(f"Loaded Cogs: {list(bot.cogs.keys())}")