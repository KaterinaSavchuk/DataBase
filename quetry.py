import sqlite3

conn = sqlite3.connect("id_software_games.db")
cursor = conn.cursor()

def execute_query(query, params=()):
    try: 
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Помилка при виконанні запиту: {e}")
    
print("\nВсі ігри з роком виходу після 2000")
execute_query("""
    SELECT game_name, release_date
    FROM games
    WHERE release_date > '2000-01-01'
    ORDER BY release_date ASC
""")

print("\nІгри, у яких видавець починається на 'B'")
execute_query("""
    SELECT DISTINCT d.publisher
    FROM devices_and_publishers d
    WHERE d.publisher LIKE 'B%'
""")

print("\nКількість ігор для кожної платформи PC")
execute_query("""
    SELECT pc_platform, COUNT(*)
    FROM (
        SELECT TRIM(value) AS pc_platform
        FROM devices_and_publishers, 
             json_each('[' || REPLACE(pc, ',', '","') || ']')
    )
    GROUP BY pc_platform
    ORDER BY COUNT(*) DESC
""")

print("\nІгри, де платформи консолей містять 'Xbox'")
execute_query("""
    SELECT g.game_name, d.consoles
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%Xbox%'
""")

print("\nІгри, які підтримують MacOS")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.pc LIKE '%macOS%'
""")

print("\nВидавці, які мають ігри як на PC, так і на консолях")
execute_query("""
    SELECT DISTINCT d.publisher
    FROM devices_and_publishers d
    WHERE d.pc != '' AND d.consoles != ''
""")

print("\nІгри, випущені у 2010 році")
execute_query("""
    SELECT game_name, release_date
    FROM games
    WHERE release_date BETWEEN '2010-01-01' AND '2010-12-31'
""")

print("\nІгри, які підтримують Windows")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.pc LIKE '%Windows%'
""")

print("\nКількість ігор для кожного року")
execute_query("""
    SELECT strftime('%Y', release_date) AS year, COUNT(*) AS games_count
    FROM games
    GROUP BY year
    ORDER BY year DESC
""")

print("\nІгри без підтримки консолей")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles = ''
""")

print("\nІгри, де видавець містить 'Apogee'")
execute_query("""
    SELECT g.game_name, d.publisher
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.publisher LIKE '%Apogee%'
""")

print("\nВидавці, які випустили лише одну гру")
execute_query("""
    SELECT d.publisher, COUNT(*) AS cnt
    FROM devices_and_publishers d
    GROUP BY d.publisher
    HAVING cnt = 1
""")

print("\nІгри з найбільшою кількістю платформ PC")
execute_query("""
    SELECT g.game_name,
           LENGTH(d.pc) - LENGTH(REPLACE(d.pc, ',', '')) + 1 AS pc_count
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    ORDER BY pc_count DESC
    LIMIT 5
""")

print("\nІгри, які підтримують Linux і macOS одночасно")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.pc LIKE '%Linux%' AND d.pc LIKE '%macOS%'
""")

print("\nСередній рік виходу ігор")
execute_query("""
    SELECT AVG(strftime('%Y', release_date)) AS avg_year
    FROM games
""")

print("\nІгри, що вийшли між 1995 і 2005 роками")
execute_query("""
    SELECT game_name, release_date
    FROM games
    WHERE release_date BETWEEN '1995-01-01' AND '2005-12-31'
""")

print("\nВидавці, чиї ігри підтримують Switch")
execute_query("""
    SELECT DISTINCT d.publisher
    FROM devices_and_publishers d
    WHERE d.consoles LIKE '%Switch%'
""")

print("\nІгри, які підтримують PS3 або Xbox 360")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%PS3%' OR d.consoles LIKE '%Xbox 360%'
""")

print("\nВсі ігри, відсортовані за довжиною назви (спадання)")
execute_query("""
    SELECT game_name, LENGTH(game_name) AS len
    FROM games
    ORDER BY len DESC
""")

print("\nІгри, де у видавця в назві слово 'Bethesda'")
execute_query("""
    SELECT g.game_name, d.publisher
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.publisher LIKE '%Bethesda%'
""")

print("\nКількість ігор на PC для кожного видавця")
execute_query("""
    SELECT d.publisher, COUNT(*)
    FROM devices_and_publishers d
    WHERE d.pc != ''
    GROUP BY d.publisher
    ORDER BY COUNT(*) DESC
""")

print("\nІгри, які підтримують Nintendo 64")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%N64%'
""")

print("\nІгри без року виходу")
execute_query("""
    SELECT game_name
    FROM games
    WHERE release_date IS NULL
""")

print("\nВидавці, які підтримують більше 5 ігор")
execute_query("""
    SELECT d.publisher, COUNT(*) AS cnt
    FROM devices_and_publishers d
    GROUP BY d.publisher
    HAVING cnt > 5
""")

print("\nІгри з підтримкою VR (віртуальна реальність)")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.pc LIKE '%VR%' OR d.consoles LIKE '%VR%'
""")

print("\nІгри, де рік виходу до 1990")
execute_query("""
    SELECT game_name, release_date
    FROM games
    WHERE release_date < '1990-01-01'
""")

print("\nВидавці, які мають ігри на платформі Windows")
execute_query("""
    SELECT DISTINCT d.publisher
    FROM devices_and_publishers d
    WHERE d.pc LIKE '%Windows%'
""")

print("\nІгри з платформою Sega 32X")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%Sega 32X%'
""")

print("\nІгри, які підтримують PS5")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%PS5%'
""")

print("\nІгри, що підтримують консолі Series X|S")
execute_query("""
    SELECT g.game_name
    FROM games g
    JOIN devices_and_publishers d ON g.game_id = d.game_id
    WHERE d.consoles LIKE '%Series X|S%'
""")
