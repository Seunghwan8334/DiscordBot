from discord.ext import commands
from Database import GUILD_INFO_LIST

# 사용 예시
# GuildDataLoader = bot.get_cog("GuildDataLoader")
# serverlog_channel = GuildDataLoader.guildInfo[member.guild.id].serverlog_channel

class Guild():
    def __init__(self, guild, serverlog_channel, welcome_channel, standard_role, standard_channel):
        self.guild = guild
        self.serverlog_channel = serverlog_channel
        self.welcome_channel = welcome_channel
        self.standard_role = standard_role
        self.standard_channel = standard_channel

class GuildDataLoader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.guildInfo = {}

    def load_all_guild_database(self):
        print(f"There's total of {len(GUILD_INFO_LIST)} guilds in database")
        for GUILD_INFO in GUILD_INFO_LIST:
            error_count = 0
            guild = self.bot.get_guild(GUILD_INFO["GUILD_ID"])
            if not guild:
                print(f"guild with {guild.id} not found")
                error_count += 1

            serverlog_channel = self.bot.get_channel(GUILD_INFO["SERVERLOG_CHANNEL_ID"])
            if not serverlog_channel:
                print(f"serverlog_channel({serverlog_channel.id}) in guild({guild.id}) not found")
                error_count += 1 

            welcome_channel = self.bot.get_channel(GUILD_INFO["WELCOME_CHANNEL_ID"])
            if not welcome_channel:
                print(f"welcome_channel({welcome_channel.id}) in guild({guild.id}) not found")
                error_count += 1 

            standard_role = guild.get_role(GUILD_INFO["STANDARD_ROLE_ID"])
            if not standard_role:
                print(f"standard_role({standard_role.id}) in guild({guild.id}) not found")
                error_count += 1 

            standard_channel = self.bot.get_channel(GUILD_INFO["STANDARD_CHANNEL_ID"])
            if not standard_channel:
                print(f"standard_channel({standard_channel.id}) in guild({guild.id}) not found")
                error_count += 1 
            
            print(f"Total of {error_count} errors found in guild({guild.id})")

            self.guildInfo[GUILD_INFO["GUILD_ID"]] = Guild(
                guild,
                serverlog_channel,
                welcome_channel,
                standard_role,
                standard_channel
            )

async def setup(bot):
    await bot.add_cog(GuildDataLoader(bot))
