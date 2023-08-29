import random

from steam_api_wrapper.classes import Game
from steam_api_wrapper.classes import GameCollection

from steam_api_wrapper.exceptions import GameSchemaIsEmptyException


def convert_list_to_games(games_list):
    games = []
    for game in games_list:
        games.append(Game(appid=game.get("appid"), total_playtime=game.get("playtime_forever")))

    return games


class GamesManager:

    @staticmethod
    def unwrap_user_game_response(game_response):
        unwrapped_response = game_response.get("response")
        game_count = unwrapped_response.get("game_count")
        game_list = convert_list_to_games(unwrapped_response.get("games"))
        games = GameCollection(game_count, game_list)
        return games

    @staticmethod
    def unwrap_personal_achievement_response(achievement_response):
        unwrapped_response = achievement_response.get("response")
        unwrapped_response = unwrapped_response.get("playerstats")
        return {"gameName": unwrapped_response.get("gameName"), "achievements": unwrapped_response.get("achievements")}

    @staticmethod
    def unwrap_game_schema_response(schema_response):
        if schema_response["game"] is False:
            print(schema_response)
            raise GameSchemaIsEmptyException

        return schema_response.get("game")

    @staticmethod
    def add_achievements_to_game(game, achievements):
        if game.name is False:
            game.name = achievements.get("gameName")

        if game.game_achievements is False:
            game.game_achievements = achievements[achievements]
        return game

    @staticmethod
    def get_random_game(game_list):
        rand_index = random.randint(0, len(game_list))
        return game_list[rand_index]

    @staticmethod
    def add_schema_info_to_game(game, game_schema):
        game.name = game_schema.get("gameName")
        game.game_stats = game_schema.get("availableGameStats")
        return game
