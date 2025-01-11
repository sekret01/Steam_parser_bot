"""
Basic commands for creating and deleting tables.
Not used during program operation
It is not recommended to perform them unnecessarily, it is possible
database data loss
"""


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


if __name__ == "__main__":
    _delete_tables()
    _create_steam_games_table()
    _create_steam_discount_table()
