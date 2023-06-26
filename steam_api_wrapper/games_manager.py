import random


def get_game_count(game_response):
    return game_response["game_count"]


def get_games_dict(game_response):
    return game_response["games"]


def get_random_game(game_list):
    rand_index = random.randint(0, len(game_list))
    return game_list[rand_index]


'''
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
        rand_index = random.randint(0, len(game_list))
        return game_list[rand_index]
'''
