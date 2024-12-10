from parse_steam import PriceLooker
import requests

def test_parse_looker():
    main_steam_link = "https://store.steampowered.com/app/"
    games = ['475550', '552500', '427520', '489630', '870780']
    looker = PriceLooker()
    for game in games:
        page = requests.get(main_steam_link+game)
        print(looker.get_price_info(page))


if __name__ == "__main__":
    test_parse_looker()