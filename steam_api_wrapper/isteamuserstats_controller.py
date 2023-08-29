import requests
import steam_api_wrapper.exceptions as exceptions


class ISteamUserStatsController:
    api_key = ""

    @staticmethod
    def get_global_achievement_percentages(game_id):
        achievement_request = f"https://api.steampowered.com/" \
                              f"ISteamUserStats/GetGlobalAchievementPercentagesForApp/v2/?gameid={game_id}"
        achievement_response = requests.get(achievement_request)
        status_code = achievement_response.status_code

        if status_code >= 200 or status_code < 300:
            return achievement_response.json()
        else:
            print(achievement_response)
            raise exceptions.InvalidResponseException

    @staticmethod
    def get_number_of_current_players(game_id):
        current_players_request = f"https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/" \
                                  f"?gameid={game_id}"
        current_players_response = requests.get(current_players_request)
        status_code = current_players_response.status_code

        if status_code >= 200 or status_code < 300:
            return current_players_response.json()
        else:
            print(current_players_response)
            raise exceptions.InvalidResponseException

    @staticmethod
    def get_player_achievements(app_id):
        player_achievements_request = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/" \
                                      f"?key={ISteamUserStatsController.api_key}&appid={app_id}"
        player_achievements_response = requests.get(player_achievements_request)
        status_code = player_achievements_response.status_code

        if status_code >= 200 or status_code < 300:
            return player_achievements_response.json()
        else:
            print(player_achievements_response)
            raise exceptions.InvalidResponseException

    @staticmethod
    def get_schema_for_game(app_id):
        game_schema_request = f"https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/" \
                              f"?key={ISteamUserStatsController.api_key}&appid={app_id}"
        game_schema_response = requests.get(game_schema_request)
        status_code = game_schema_response.status_code

        if status_code >= 200 or status_code < 300:
            return game_schema_response.json()
        else:
            print(game_schema_response)
            raise exceptions.InvalidResponseException

    @staticmethod
    def get_user_stats_for_game(profile_id, app_id):
        user_stats_for_game_request = f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/" \
                                      f"?key={ISteamUserStatsController.api_key}" \
                                      f"&steamid={profile_id}" \
                                      f"&appid={app_id}"
        user_stats_for_game_response = requests.get(user_stats_for_game_request)
        status_code = user_stats_for_game_response.status_code

        if status_code >= 200 or status_code < 300:
            return user_stats_for_game_response.json()
        else:
            print(user_stats_for_game_response)
            raise exceptions.InvalidResponseException
