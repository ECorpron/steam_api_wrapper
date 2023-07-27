import random
import steam_api_wrapper.classes as classes


def unwrap_user_game_response(game_response):
    unwrapped_response = game_response["response"]
    game_count = unwrapped_response["game_count"]
    game_list = convert_list_to_games(unwrapped_response["games"])
    games = classes.GameCollection(game_count, game_list)
    return games


def convert_list_to_games(games_list):
    games = []
    for game in games_list:
        games.append(classes.Game(appid=game.get("appid"), total_playtime=game.get("playtime_forever")))

    return games


def get_random_game(game_list):
    rand_index = random.randint(0, len(game_list))
    return game_list[rand_index]


def add_schema_info_to_game(game, game_schema):
    game.name = game_schema.get("gameName")
    game.game_stats = game_schema.get("availableGameStats")
    return game


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
