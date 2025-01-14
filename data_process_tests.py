from steam_database import DatabaseController, DatabaseGetter
from parse_steam import GameParser
from time import time


gp = GameParser()
dg = DatabaseGetter()
games = [
    "https://store.steampowered.com/app/649950/Ashen/",
    "https://store.steampowered.com/app/1951230/Pizza_Possum/",
    "https://store.steampowered.com/app/1282100/REMNANT_II/",
    "https://store.steampowered.com/app/677160/We_Were_Here_Too/",
    "https://store.steampowered.com/app/1001270/Kebab_Chefs__Restaurant_Simulator/",
    "https://store.steampowered.com/app/638230/Journey/",
    "https://store.steampowered.com/app/837470/Untitled_Goose_Game/"
]

start = time()
for game in games:
    gp.save_new_game(game)
print(round(time() - start, 2))

print(f"\nGAMES\n")
print(*dg.get_all_games_list(), sep='\n')
print(f"\nDISCOUNTS\n")
print(*dg.get_all_discount_games(), sep='\n')

