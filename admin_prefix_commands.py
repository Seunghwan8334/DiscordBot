from initializations import *

@bot.command(name="shutdown")  
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send("shutting down...") 
    await bot.close() 

@bot.command(name="info") 
@commands.has_permissions(administrator=True)
async def info(ctx, *, member: discord.Member):
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)-1} roles.'
    await ctx.send(msg)
    await ctx.send("roles are") 
    for role in member.roles:
        if role.is_default():
            continue
        await ctx.send(role) 

@bot.command(name="say")
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