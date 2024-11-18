from initializations import *

commands_list = [
    "help",
    "$test1",
    "$test2 (arg1)",
    "$shutdown",
] 

#bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="commands") 
async def commands_(ctx):
    await ctx.send("Here are the commands list")
    commands_text = "\n".join(commands_list)
    await ctx.send(commands_text)

@bot.command(name="test") 
async def test(ctx):
    await ctx.send("정상 가동 중..")

@bot.command(name="test1") 
async def test1(ctx):
    await ctx.send("This is a prefix test command!")

@bot.command(name="test2")
async def test2(ctx, arg1):
    await ctx.send(f"You passed {arg1} !")

@bot.command(name="shutdown", help="shutdowns bot")  
@commands.has_permissions(administrator=True)
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


@bot.command(name="server")
async def server(ctx):
    await ctx.send(ctx.guild)

@bot.command(name="add") #Basic converter
async def add(ctx, a: int,b: int):
    await ctx.send(a+b)

@bot.command(name="info") 
async def info(ctx, *, member: discord.Member):
    msg = f'{member} joined on {member.joined_at} and has {len(member.roles)-1} roles.'
    await ctx.send(msg)
    await ctx.send("roles are") 
    for role in member.roles:
        if role.is_default():
            continue
        await ctx.send(role) 
