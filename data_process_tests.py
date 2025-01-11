from steam_database import DatabaseController, DatabaseGetter

dc = DatabaseController()
dg = DatabaseGetter()

dc.add_new_game("1", "1", "111", "asjdhikouasd")
print(dg.get_all_games_list())

dc.set_game_discount("22", "21 руб.", "-30%", "end in 21 december")
print(dg.get_discount_games())

input()

dc.delete_game("1")
print(dg.get_all_games_list())


dc.unset_game_discount("22")
print(dg.get_discount_games())