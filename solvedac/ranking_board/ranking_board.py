from discord.ext import commands
import sqlite3

class RankingBoard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        self.ranking_board = None
        self.user_list = []
    
    @commands.command(name="ranking_board")
    @commands.is_owner()
    async def rank_board(self, ctx):
        pass

    def update_ranking_board(self):    
        conn = sqlite3.connect("solved.ac/ranking_board/database.db")
        cursor = conn.cursor()

        table_name = "users"

        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        user_list = []

        for row in rows:
            discord_user_id = row[0]
            baekjoon_user_name = row[1]
            user_list.append({
                "discord_user_id" : discord_user_id,
                "baekjoon_user_name" : baekjoon_user_name,
            })
        conn.close()

        self.user_list = user_list




    def generate_message(self):
        pass

    
async def setup(bot):
    await bot.add_cog(RankingBoard(bot))