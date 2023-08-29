from steam_api_wrapper.iplayerservice_controller import IPlayerServiceController
from steam_api_wrapper.isteamuserstats_controller import ISteamUserStatsController
from steam_api_wrapper.games_manager import GamesManager
from steam_api_wrapper.classes import Account

import credentials.config

profile_id = "76561198046373486"
steam_api_key = credentials.config.steam_api_key
my_account = Account(profile_id=profile_id)

IPlayerServiceController.api_key = steam_api_key
ISteamUserStatsController.api_key = steam_api_key


def get_random_game_with_name(games):
    game = None
    name = ""
    while not name:
        game = GamesManager.get_random_game(games.game_list)
        random_game_info = ISteamUserStatsController.get_schema_for_game(game.appid)
        unwrapped_game_info = GamesManager.unwrap_game_schema_response(random_game_info)
        game = GamesManager.add_schema_info_to_game(game, unwrapped_game_info)
        name = game.name

        if name is False:
            backup = ISteamUserStatsController.get_player_achievements(game.appid)
            achievements = GamesManager.unwrap_personal_achievement_response(backup)
            game = GamesManager.add_achievements_to_game(game, achievements)
    return game


my_games_response = IPlayerServiceController.get_owned_games_request(profile_id, False)

my_games = GamesManager.unwrap_user_game_response(my_games_response)
print("My games: ", my_games)

print("\nNumber of games: ", my_games.game_count)

print("\nList of Games: \n", my_games.game_list)

rand_game = get_random_game_with_name(my_games)

print("\nRandom Game: ", rand_game)
