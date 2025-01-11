from steam_database import DatabaseController
from parse_steam import NameScanner, PriceScaner
import requests


class GameParser:
    """
    Searching and recording information
    about the new game
    """

    def __init__(self):
        self.controller = DatabaseController()
        self.name_getter = NameScanner()
        self.price_getter = PriceScaner()

    def save_main_info(self, game_id: str, name: str, url: str, price: str):
        self.controller.add_new_game(game_id, name, price, url)

    def set_game_discount(self, game_id, discount_info: tuple[str, str, str]):
        discount_price, percents, discount_info = discount_info
        self.controller.set_game_discount(game_id, discount_price, percents, discount_info)

    def save_new_game(self, url: str) -> None:
        """
        Saving information about a new game
        in the database

        :param url: link to the game page on steam
        :return: None
        """

        page = requests.get(url=url)
        game_name, game_url = self.name_getter.get_new_game_info(page)
        discount, origin_price, discount_data = self.price_getter.get_price_info(page)
        game_id = url.replace("//", "/").split('/')[3]

        self.save_main_info(game_id, game_name, game_url, origin_price)
        if discount:
            self.set_game_discount(game_id, discount_data)

