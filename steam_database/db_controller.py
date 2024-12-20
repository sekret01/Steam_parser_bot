import sqlite3


class DatabaseController:
    def __init__(self):
        self.db_path = "steam_database.db"

    def add_new_game(self, game_id: str, game_name: str, price: str, link: str):
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute(f"""
        INSERT INTO Games VALUES
        ({game_id}, {game_name}, {price}, {link})
        """)
        db.close()

    def delete_game(self):
        pass

    def set_game_discount(self):
        pass

    def unset_game_discount(self):
        pass
