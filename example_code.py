import steam_api_wrapper.steam_api_controller as steam_api
import steam_api_wrapper.games_manager as owned_games

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

my_api = steam_api.SteamAPIController(api_key=steam_api_key, profile_id=profile_id)
my_games_response = my_api.owned_game_request()

my_games = my_games_response["response"]

game_count = owned_games.get_game_count(my_games)
game_list = owned_games.get_games_dict(my_games)
print("Number of games: " + str(game_count))

print("List of Games: \n" + str(game_list))

rand_game = owned_games.get_random_game(game_list)

print(rand_game.get("name"))

game = classes.Game(rand_game.get("appid"),
                    rand_game.get("name"),
                    rand_game.get("playtime_forever"))
print(game)
