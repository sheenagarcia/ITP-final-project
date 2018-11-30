class GameStats():
    """Track statistics of Shoot the Fish"""

    def __init__(self, ai_settings):
        """Initialize settings"""
        self.ai_settings = ai_settings
        self.reset_stats()

    #Most stats (i.e. number of lives left, etc.) need to reset when you start a new game, so they'll be under here
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.mermaids_left = self.ai_settings.mermaid_limit
        
