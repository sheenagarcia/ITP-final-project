class Settings():
    """A class to store all settings for Shoot the Fish"""

    def __init__(self):
        """Initialize game settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (212, 230, 241)

        #Mermaid Settings
        self.mermaid_speed_factor = 1.5

        #Bubble Settings
        self.bubble_speed_factor = 1
        self.bubble_width = 10
        self.bubble_height = 10
        self.bubble_colour = 46, 134, 193
        self.bubbles_allowed = 3
