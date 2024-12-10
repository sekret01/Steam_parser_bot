from __future__ import annotations
from bs4 import BeautifulSoup
from requests import Response


class PriceLooker:
    """Price parsing and discount search class"""
    def __init__(self):
        self.price_block: BeautifulSoup = BeautifulSoup()

    def is_discount(self):
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
        soup = BeautifulSoup(page.text, "html.parser")
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

