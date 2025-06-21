import sqlite3
import json
from datetime import datetime

def parse_date_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

conn = sqlite3.connect("id_software_games.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS id_software_games (
        game_id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_name TEXT NOT NULL,
        release_date DATE
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices_and_publishers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        game_id INTEGER,
        pc TEXT,
        consoles TEXT,
        publisher TEXT,
        FOREIGN KEY (game_id) REFERENCES id_software_games(game_id) ON DELETE CASCADE
    );
""")

with open("id_software_games_full.json", "r", encoding="utf-8") as f:
    games_data = json.load(f)

for game in games_data:
    game_name = game["title"]
    release_date = f"{game['year']}-01-01"
    pc = ", ".join(game["platforms_pc"])
    consoles = ", ".join(game["platforms_console"])
    publisher = game["publisher"]

    cursor.execute("""
        INSERT INTO id_software_games (game_name, release_date)
        VALUES (?, ?)
    """, (game_name, parse_date_safe(release_date)))

    game_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO devices_and_publishers (game_id, pc, consoles, publisher)
        VALUES (?, ?, ?, ?)
    """, (game_id, pc, consoles, publisher))

conn.commit()
conn.close()

print("Данні успішно додані в базу!")
