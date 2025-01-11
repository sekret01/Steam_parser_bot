from __future__ import annotations
import requests
from bs4 import BeautifulSoup
from requests import Response
from .price_looker import PriceLooker


class GameParser:
    """
    Finding basic information about the game:
     - name
     - link
    """

    def __init__(self) -> None:
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "upgrade-insecure-requests": "1"
        }
        self.session = requests.Session()
        self.price_looker = PriceLooker()


    def _get_games_name(self, page: Response) -> str:
        soup = BeautifulSoup(page.text, 'html.parser')
        name = soup.find("div", id="appHubAppName").text
        return name

    def add_new_game(self, url: str) -> tuple[str, str]:
        """
        Adding information about a new game to the database

        The search for information occurs on the link page, which
        was indicated


        :param url: link to the page with the game you want
        :return: None
        """

        page = self.session.get(url=url, headers=self.headers)
        game_name = self._get_games_name(page)
        game_url = url

        return game_name, game_url


g = GameParser()
g.add_new_game("https://store.steampowered.com/app/2559270/Gym_Simulator_24/")