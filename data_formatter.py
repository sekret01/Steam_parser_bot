from steam_database import DatabaseGetter

class DataFormatter:
    """ ... """

    def __init__(self):
        self.getter = DatabaseGetter()

    def formatting_message(self, data: tuple):
        """ generates an easy to read string of information """
        return (f"{data[0]}\n"
                f"{data[1]} ({data[2]})  ->  {data[3]}\n"
                f"{data[4]}\n"
                f"{data[5]}")

    def print_start_discount(self, game_id: str) -> str:
        """
        Returns a string with information about the specified game

        :param game_id: game code
        :return: line with information
        """

        data = self.getter.get_discount_game(game_id=game_id)
        if len(data) == 0: return ""
        return self.formatting_message(data[0])


    def get_discounts_info(self) -> list:
        """ Возвращает список строк с информацией о всех играх со скидкой """

        all_data = self.getter.get_all_discount_games()
        if len(all_data) == 0: return []

        res = []
        for game in all_data:
            res.append(self.formatting_message(game))
        return res
