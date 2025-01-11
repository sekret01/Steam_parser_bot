from __future__ import annotations
from bs4 import BeautifulSoup
from requests import Response


class PriceScaner:
    """
    Price parsing and discount search class

    For price information use only
    get_price_info() function. Other functions are auxiliary and
    are used to collect individual pieces of information about the game.
    """

    def __init__(self) -> None:
        self.price_block: BeautifulSoup = BeautifulSoup()

    def is_discount(self) -> bool:
        if self.price_block is None: return False
        if self.price_block.find("div", class_="discount_prices"):
            return True
        return False

    def get_origin_price(self) -> str:
        return self.price_block.find("div", class_="game_purchase_price price").text.strip()

    def get_discount_info(self) -> tuple[str, str, str, str]:
        origin_price = self.price_block.find("div", class_="discount_original_price").text.strip()
        discount_price = self.price_block.find("div", class_="discount_final_price").text.strip()
        percents = self.price_block.find("div", class_="discount_pct").text.strip()
        discount_info = self.price_block.find("p", class_="game_purchase_discount_countdown").text.strip()
        return origin_price, discount_price, percents, discount_info

    def get_price_info(self, page: Response) -> tuple[int, str, any]:
        """
        Parses the received page, finds the necessary information

        :param page: the page on which the search is conducted
        :return: data tuple; may have one of the following types:

                <discount availability> == 1
                ... -> (<discount availability>, <price>, (<discount price>, <discount percentage>, <discount end information>))

                <discount availability> == 0
                ... -> (<availability of discount>, <price>, None)
        """
        soup = BeautifulSoup(page.text, "html.parser")

        # game not release yet
        not_yet_block = soup.find("span", class_="not_yet")
        if not_yet_block:
            return 0, "игра не вышла", None

        self.price_block = soup.find("div", class_="game_area_purchase_game_wrapper")

        if self.is_discount():
            discount = 1
            origin_price, discount_price, percents, discount_info = self.get_discount_info()
            discount_data = (discount_price, percents, discount_info)
        else:
            if self.price_block is None: self.price_block = soup
            discount = 0
            origin_price = self.get_origin_price()
            discount_data = None

        return discount, origin_price, discount_data

