class Account:
    def __init__(self, profile_id, game_count=0, game_list=None):
        if game_list is None:
            game_list = {}
        self.profile_id = profile_id
        self.game_count = game_count
        self.game_list = game_list


class Game:
    def __init__(self, appid, name="", total_playtime=0, game_stats=None, game_achievements=None):
        self.game_achievements = game_achievements
        self.appid = appid
        self.name = name
        self.total_playtime = total_playtime
        self.game_stats = game_stats

    def __str__(self):
        output = "appid: {}\n".format(self.appid)
        output = output + "name: {}\n".format(self.name)
        output = output + "Total Playtime: {}\n".format(self.total_playtime)
        output = output + "Game Stats: {}\n".format(self.game_stats)
        output = output + "Game Achievements: {}".format(self.game_achievements)
        return output

    def __repr__(self):
        output = "{"
        output = output + "appid: {}, ".format(self.appid)
        output = output + "name: {}, ".format(self.name)
        output = output + "Total Playtime: {}, ".format(self.total_playtime)
        output = output + "Game Stats: {}".format(self.game_stats)
        output = output + "Game Achievements: {}".format(self.game_achievements)
        output = output + "}"
        return output


class GameCollection:
    def __init__(self, game_count=0, game_list=None):
        self.game_count = game_count
        self.game_list = game_list

    def __repr__(self):
        output = "{"
        output = output + "game_count: {}, ".format(self.game_count)
        output = output + "game_list: {}, ".format(self.game_list)
        output = output + "}"
        return output
