from requests import session

from parse_steam import PriceLooker
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
    ("2397300", (0, )) # невышедшая игра
])
def test_parse_looker(game_code, result, get_session):
    main_steam_link = "https://store.steampowered.com/app/"
    session = get_session
    page = session.get(main_steam_link + game_code)
    looker = PriceLooker()
    assert looker.get_price_info(page=page) == result



if __name__ == "__main__":
    test_parse_looker()