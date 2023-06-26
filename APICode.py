import classes.game as game
import classes.account as account

import steam_api.steam_api_controller as api
import steam_api.owned_game_controller as game_controller

profile_id = "76561198046373486"
my_account = account.Account(profile_id=profile_id)


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

my_api = api.SteamAPIController(profile_id)
my_games_response = my_api.owned_game_request()

# print(my_games)

my_games = my_games_response["response"]

game_count = game_controller.get_game_count(my_games)
game_list = game_controller.get_games_dict(my_games)
print("Number of games: " + str(game_count))

print("List of Games: \n" + str(game_list))

rand_game = game_controller.get_random_game(game_list)

print(rand_game.get("name"))

game = game.Game(rand_game.get("appid"),
                 rand_game.get("name"),
                 rand_game.get("playtime_forever"))
print(game)
