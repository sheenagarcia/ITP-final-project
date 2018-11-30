class GameStats():
    """Track statistics of Shoot the Fish"""

    def __init__(self, ai_settings):
        """Initialize settings"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Start Shoot the Fish in inactive state
        self.game_active = False #when this is false (at beginning + when mermaids_left =< 0), you stop the game

    #Most stats (i.e. number of lives left, etc.) need to reset when you start a new game, so they'll be under here
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.mermaids_left = self.ai_settings.mermaid_limit
        self.score = 0 #to reset each time, put it under this function instead of __init__
        self.level = 1
