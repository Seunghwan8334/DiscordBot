from initializations import bot

@bot.command(name="test") 
async def test(ctx):
    await ctx.send("정상 가동 중..")

@bot.command(name="server")
async def server(ctx):
    await ctx.send(ctx.guild)

@bot.command(name="add") 
async def add(ctx, a: int,b: int):
    await ctx.send(a+b)



