import sqlite3

conn = sqlite3.connect("solvedac/ranking_board/database.db")
cursor = conn.cursor()

with open("solvedac/ranking_board/db_query.sql", "r") as file:
    sql_script = file.read()
    cursor.executescript(sql_script)

conn.commit()
conn.close()
