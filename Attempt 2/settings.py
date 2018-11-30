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
        self.mermaid_limit = 3

        #Bubble Settings
        self.bubble_speed_factor = 3
        self.bubble_width = 300
        self.bubble_height = 15
        self.bubble_colour = 46, 134, 193
        self.bubbles_allowed = 3

        #Fish Settings
        self.fish_speed_factor = 1
        self.school_drop_speed = 10 #controls how fast fish drop
        self.school_direction = 1 #1 = right, -1 = left
