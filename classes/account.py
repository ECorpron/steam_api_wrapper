class Account:
    def __init__(self, profile_id, game_count=0, game_dict=None):
        if game_dict is None:
            game_dict = {}
        self.profile_id = profile_id
        self.game_count = game_count
        self.game_dict = game_dict
