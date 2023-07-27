import json

import steam_api_wrapper.iplayerservice_controller as player_service
import steam_api_wrapper.isteamuserstats_controller as steam_user_service
import steam_api_wrapper.games_manager as games_manager

import steam_api_wrapper.classes as classes
import credentials.config

profile_id = "76561198046373486"
steam_api_key = credentials.config.steam_api_key
my_account = classes.Account(profile_id=profile_id)

# profile = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steam_api_key}&steamids={
# profile_id}" achievement_request =\
# 'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=440' friends_list
# = \ f" http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steam_api_key}&steamid={
# profile_id}&relationship=friend"

# print(friendsList)

# response = requests.get(profile)
# r = requests.get('https://api.github.com/events')
# games = requests.get(gameRequest)
# friends = requests.get(friendsList)

# input_json = {'steamid': profile_id, 'include_played_free_games': False}
# input_json = json.dumps(input_json)

# print(input_json)

test_dict = {'appid': 3920, 'playtime_forever': 0, 'playtime_windows_forever': 0, 'playtime_mac_forever': 0, 'playtime_linux_forever': 0, 'rtime_last_played': 0, 'playtime_disconnected': 0}
print(test_dict.get("appid"))


player_service.IPlayerServiceController.api_key = steam_api_key

my_games_response = player_service.IPlayerServiceController.get_owned_games_request(profile_id, False)

my_games = games_manager.unwrap_user_game_response(my_games_response)
print(my_games)

print("Number of games: ", my_games.game_count)

print("List of Games: \n", my_games.game_list)

rand_game = games_manager.get_random_game(my_games.game_list)
print("Random Game: \n")
print(rand_game)


steam_user_service.ISteamUserStatsController.api_key = steam_api_key

random_game_info = steam_user_service.ISteamUserStatsController.get_schema_for_game(rand_game.appid)

random_game = games_manager.add_schema_info_to_game(rand_game, random_game_info)

print(random_game_info)
