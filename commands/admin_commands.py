from discord.ext import commands

class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="shutdown")
    @commands.is_owner()
    async def shutdown(self, ctx):
        HufsMonitor = self.bot.get_cog("HufsMonitor")
        if HufsMonitor.monitor_status == True:
            await HufsMonitor.monitor_off(ctx)
        await ctx.send("shutting down...")
        await self.bot.close()

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync(self, ctx):
        await self.bot.tree.sync(guild=ctx.guild)

    @commands.command(name="clear")
    @commands.is_owner()
    async def clear(self, ctx, num:int):
        if num < 1:
            await ctx.channel.send("1 이상의 숫자를 입력해주세요.") 
        elif num > 20:
            await ctx.channel.send("최대 20개의 메세지까지 지울 수 있습니다.")
        else:
            deleted = await ctx.channel.purge(limit=num+1)
            await ctx.channel.send(f"{len(deleted)-1}개의 메세지를 삭제하였습니다.(2초 후 삭제)",delete_after=2)

    @commands.command(name="say")
    @commands.is_owner()
    async def say(self, ctx, *, args):
        if ctx.author == self.bot.user:
            await ctx.channel.send("무한반복 감지!!")
        try:
            parts = args.split()
            if parts[-1].startswith("<#") and parts[-1].endswith(">"):
                message_content = " ".join(parts[:-1])
                channel_id = int(parts[-1][2:-1])
                target_channel = self.bot.get_channel(channel_id)

                if target_channel:
                    await target_channel.send(message_content)
                    await ctx.channel.send(f"메세지를 {target_channel.mention}에 보냈습니다.")
                else:
                    await ctx.channel.send(f"해당 채널을 찾을 수 없습니다.")
            else:
                await ctx.channel.send(f"명령어 형식을 따라해주세요.\n$say [메세지] [보낼채널]")  
        except Exception as e:
            await ctx.send(f"오류가 발생했습니다: {e}")


async def setup(bot):
    await bot.add_cog(AdminCommands(bot))


