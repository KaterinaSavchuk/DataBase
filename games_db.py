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
    CREATE TABLE IF id_software_games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_name TEXT,
    relese_date DATE,
    );
    """)

cursor.execute("""
    CREATE TABLE IF devices_and_publishers (
    PC TEXT,
    consoles TEXT,
    publishers TEXT,
    FOREIGN KEY (game_id) REFERENCES id_software_games(game_id) ON DELETE CASCADE
    );
    """)

with open("", "r", encoding="utf-8"
) as f:
    id_software_games = json.load(f)
    
for game in id_software_games: 
    cursor.execute("""
        INSERT INTO  id_software_games (
            game_name, relese_date,
    
    )
    
    VALUES ( ?, ?)
    
    """, (
        game["game_name"],
        parse_date_safe(game["relese_date"])
        ))

game_id = cursor.lastrowid

cursor.execute("""
    INSERT INTO  id_software_games (
    PC, consoles,
    publishers,
    
)
    
VALUES ( ?, ?, ?)
    
""", (
    game["PC"],
    game["consoles"],
    game["publishers"],
    ))

conn.commit()
conn.close()

print("Дані успішно додані!")
