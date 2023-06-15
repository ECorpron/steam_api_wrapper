import random

class OwnedGamesManager:

    def __init__(self):
        pass

    @staticmethod
    def get_game_count(game_response):
        return game_response["game_count"]

    @staticmethod
    def get_games_dict(game_response):
        return game_response["games"]

    @staticmethod
    def get_random_game(game_list):
        rand_game = random.randint(0, len(game_list))
