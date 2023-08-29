import json

import requests
from steam_api_wrapper.exceptions import InvalidResponseException


class IPlayerServiceController:
    api_key = ""

    @staticmethod
    def get_player_summaries_request(profile_id):
        profile_request = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/" \
                          f"?key={IPlayerServiceController.api_key}" \
                          f"&steamids={profile_id}"

        profile_response = requests.get(profile_request)
        status_code = profile_response.status_code

        if status_code == 200:
            return profile_response.json()
        else:
            print(profile_response)
            raise InvalidResponseException

    @staticmethod
    def get_owned_games_request(profile_id, include_free_games):
        input_json = {'steamid': profile_id, 'include_played_free_games': include_free_games}
        input_json = json.dumps(input_json)

        owned_games_request = f" https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/" \
                              f"?key={IPlayerServiceController.api_key}" \
                              f"&input_json={input_json}"

        game_response = requests.get(owned_games_request)
        status_code = game_response.status_code

        if status_code >= 200 or status_code < 300:
            return game_response.json()
        else:
            print(game_response)
            raise InvalidResponseException

    @staticmethod
    def get_recent_played_games_request(profile_id):
        input_json = {'steamid': profile_id}
        input_json = json.dumps(input_json)
        recent_games_request = f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/" \
                               f"?key={IPlayerServiceController.api_key}" \
                               f"&input_json={input_json}"

        recent_games_response = requests.get(recent_games_request)
        status_code = recent_games_response.status_code

        if status_code >= 200 or status_code < 300:
            return recent_games_response.json()
        else:
            print(recent_games_response)
            raise InvalidResponseException
