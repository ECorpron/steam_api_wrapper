import requests
import random

import modules.classes as c
import modules.steam_calls as api

key = "2C37C1FD41653A578C221683DCC06B6F"
profile_id = "76561198046373486"

profile = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={profile_id}"
achievement_request =\
    'http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=440'
friends_list = \
    f" http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={profile_id}&relationship=friend"

owned_games = f" http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/" \
              f"?key={key}&steamid={profile_id}&format=json&include_appinfo=true&include_played_free_games=true"

#print(friendsList)

#response = requests.get(profile)
#r = requests.get('https://api.github.com/events')
#games = requests.get(gameRequest)
#friends = requests.get(friendsList)
my_games = requests.get(owned_games)

json_games = my_games.json()

print("Status Code: "+str(my_games.status_code))
#print("JSON version of response: \n"+str(jsonGames))

#print("Text version of response: \n"+myGames.text)


print(len(json_games))
#print(jsonGames["response"])
#print(type(jsonGames["response"]))

response_body = json_games["response"]

#print("response Body: \n"+str(responseBody))
print("Length of response body: "+str(len(response_body)))

game_count = response_body["game_count"]
game_list = response_body["games"]
print("Number of games: "+str(game_count))

print("List of Games: \n"+str(game_list))

rand_game = random.randint(0, game_count)

print(game_list[rand_game])
print(game_list[rand_game].get("name"))

game = c.Game(game_list[rand_game].get("appid"),
              game_list[rand_game].get("name"),
              game_list[rand_game].get("playtime_forever"))
print(game)
