class Account:
    def __init__(self, profile_id, game_count=0, game_dict=None):
        if game_dict is None:
            game_dict = {}
        self.profile_id = profile_id
        self.game_count = game_count
        self.game_dict = game_dict


class Game:
    def __init__(self, appid, name, total_playtime):
        self.appid = appid
        self.name = name
        self.total_playtime = total_playtime

    def __str__(self):
        output = "appid: {}\n".format(self.appid)
        output = output + "name: {}\n".format(self.name)
        output = output + "Total Playtime: {}\n".format(self.total_playtime)
        return output


class GameCollection:

    def __init__(self, game_count=0, game_dict=None):
        pass
