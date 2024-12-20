import sqlite3


class DatabaseGetter:
    def __init__(self):
        self.db_path = "steam_database/steam_database.db"

    def get_discount_games(self):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute("""
                SELECT * FROM Discounts
                """)
        results = cursor.fetchall()
        db.close()
        return results

    def get_all_games_list(self):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute("""
        SELECT * FROM Games
        """)
        results = cursor.fetchall()
        db.close()
        return results
