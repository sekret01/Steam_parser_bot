import sqlite3
DB_PATH = "steam_database.db"


def _create_steam_games_table():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Games(
    id TEXT PRIMARY KEY,
    name TEXT,
    price TEXT,
    link TEXT
    )
    """)
    con.close()


def _create_steam_discount_table():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Discounts(
        id TEXT PRIMARY KEY,
        new_price TEXT,
        percent TEXT,
        info TEXT
        )
        """)
    con.close()


def _delete_tables():
    con = sqlite3.connect(DB_PATH)
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS Games")
    cursor.execute("DROP TABLE IF EXISTS Discounts")
    con.close()
