from parse_steam import PriceScaner
from parse_steam import NameScanner
import requests
import pytest

@pytest.fixture()
def get_session():
    session = requests.Session()
    session.headers.update({
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
                        })
    return session


@pytest.mark.parametrize("game_code, result", [
    ("427520", (0, "1200 руб.", None)),
    ("489630", (1, "1496 руб.", ("149 руб.", "-90%", "СКИДКА ВСЮ НЕДЕЛЮ! Предложение заканчивается 16 декабря"))),
    ("427520", (0, "1200 руб.", None)),
    ("305620", (1, "799 руб.", ("479 руб.", "-40%", "АКЦИЯ ПОСРЕДИ НЕДЕЛИ! Заканчивается 19 декабря"))),
    ("1671340", (0, "Бесплатно", None)),
    ("2397300", (0, "игра не вышла", None)), # невышедшая игра
    ("1363080", (1, "1499 руб.", ("1049 руб.", "-30%", "АКЦИЯ НА ВЫХОДНЫХ! Заканчивается 19 декабря"))),
    ("1818450", (0, "Бесплатно", None)),
    ("2294660", (0, "игра не вышла", None))
])
def test_prise_looker(game_code, result, get_session):
    """ THIS TEST NEEDS TO BE UPDATED DUE TO CONTINUOUS CHANGES IN GAME DISCOUNT STATUS """
    main_steam_link = "https://store.steampowered.com/app/"
    looker = PriceScaner()
    assert looker.get_price_info(main_steam_link + game_code) == result


@pytest.mark.parametrize("game_code, result", [
    ("427520", ("Factorio", "https://store.steampowered.com/app/427520")),
    ("489630", ("Warhammer 40,000: Gladius - Relics of War", "https://store.steampowered.com/app/489630")),
    ("305620", ("The Long Dark", "https://store.steampowered.com/app/305620")),
    ("1671340", ("Fears to Fathom - Home Alone", "https://store.steampowered.com/app/1671340")),
    ("2397300", ("Half Sword", "https://store.steampowered.com/app/2397300")), # невышедшая игра
    ("1363080", ("Manor Lords", "https://store.steampowered.com/app/1363080")),
    ("1818450", ("STALCRAFT: X", "https://store.steampowered.com/app/1818450")),
    ("2294660", ("The Quinfall", "https://store.steampowered.com/app/2294660"))
])
def test_game_parser(game_code, result):
    main_steam_link = "https://store.steampowered.com/app/"
    game_parser = NameScanner()
    res = game_parser.get_new_game_info(main_steam_link + game_code)
    assert res == result


if __name__ == "__main__":
    # test_prise_looker()
    test_game_parser()