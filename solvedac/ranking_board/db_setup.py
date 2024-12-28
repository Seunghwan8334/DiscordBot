import sqlite3

conn = sqlite3.connect("solved.ac/ranking_board/database.db")
cursor = conn.cursor()

with open("solved.ac/ranking_board/db_query.sql", "r") as file:
    sql_script = file.read()
    cursor.executescript(sql_script)

conn.commit()
conn.close()
