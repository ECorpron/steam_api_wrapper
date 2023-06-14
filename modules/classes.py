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

class Account:
    def __init__(self, key, profile_id):
        self.key = key
        self.profile_id = profile_id