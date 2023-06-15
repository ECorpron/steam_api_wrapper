import requests
import credentials.config as config
import exceptions.invalid_response_exception


class SteamAPIController:

    def __init__(self, profile_id):
        self.api_key = config.steam_api_key
        self.profile_id = profile_id

    def profile_request(self):
        profile_request = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/" \
                          f"?key={self.api_key}&steamids={self.profile_id}"
        profile_response = requests.get(profile_request)
        status_code = profile_response.status_code

        if status_code == 200:
            return profile_response.json()
        else:
            raise exceptions.invalid_response_exception.InvalidResponseException

    def owned_game_request(self):
        owned_games_request = f" http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}" \
                      f"&steamid={self.profile_id}&format=json&include_appinfo=true&include_played_free_games=true"

        game_response = requests.get(owned_games_request)

        status_code = game_response.status_code
        print(status_code)

        if status_code == 200:
            return game_response.json()
        else:
            raise exceptions.invalid_response_exception.InvalidResponseException

