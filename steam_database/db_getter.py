import sqlite3


class DatabaseGetter:
    """ Getting information about games from the database 'steam_database.db' """

    def __init__(self):
        self.db_path = "steam_database/steam_database.db"

    def get_all_discount_games(self):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute("""
                SELECT Games.name, Games.price, Discounts.percent, Discounts.new_price, Discounts.info, Games.link
                FROM Discounts, Games
                WHERE Discounts.id = Games.id
                """)
        results = cursor.fetchall()
        db.close()
        return results

    def get_discount_game(self, game_id: str):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute(f"""
                        SELECT Games.name, Games.price, Discounts.percent, Discounts.new_price, Discounts.info, Games.link
                        FROM Discounts, Games
                        WHERE Discounts.id = {game_id} and Discounts.id = Games.id
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
