import sqlite3


class DatabaseController:
    def __init__(self):
        self.db_path = "steam_database/steam_database.db"

    def add_new_game(self, game_id: str, game_name: str, price: str, link: str):
        """Write a new tracked game to the database"""
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        try:
            cursor.execute(f"""
            INSERT INTO Games VALUES
            (?, ?, ?, ?)
            """, (game_id, game_name, price, link))
            db.commit()
        except sqlite3.IntegrityError:
            # WARNING trying to re record the game
            pass
        db.close()

    def delete_game(self, game_id: str):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute("DELETE FROM Games WHERE id = ?", (game_id,))
        db.commit()
        db.close()

    def set_game_discount(self, game_id: str, new_price: str, percent: str, discount_info: str):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        try:
            cursor.execute("""
            INSERT INTO Discounts VALUES
            (?, ?, ?, ?)
            """, (game_id, new_price, percent, discount_info))
            db.commit()
        except sqlite3.IntegrityError:
            # WARNING trying to re record the game
            pass
        db.close()

    def unset_game_discount(self, game_id: str):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute("DELETE FROM Discounts WHERE id = ?", (game_id,))
        db.commit()
        db.close()
