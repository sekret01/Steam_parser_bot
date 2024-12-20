import sqlite3


class DatabaseController:
    def __init__(self):
        self.db_path = "steam_database.db"

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
        except sqlite3.InternalError:
            pass
        db.close()

    def delete_game(self):
        pass

    def set_game_discount(self):
        pass

    def unset_game_discount(self):
        pass
