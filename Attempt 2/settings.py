class Settings():
    """A class to store all settings for Shoot the Fish"""

    def __init__(self):
        """Initialize game'sstatic settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (212, 230, 241)

        #Mermaid Settings
        self.mermaid_limit = 3

        #Bubble Settings
        self.bubble_width = 300
        self.bubble_height = 15
        self.bubble_colour = 46, 134, 193
        self.bubbles_allowed = 3

        #Fish Settings
        self.school_drop_speed = 10 #controls how fast fish drop

        #How quickly game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize setting that change throughout game"""
        self.mermaid_speed_factor = 1.5
        self.fish_speed_factor = 1
        self.bubble_speed_factor = 3
        self.school_direction = 1 #1 = right, -1 = left

    def increase_speed(self): #multiple each speed settings by value of speedup_scale (1.1)
        """Increase speed settings"""
        self.mermaid_speed_factor *= self.speedup_scale
        self.bubble_speed_factor *= self.speedup_scale
        self.fish_speed_factor *= self.speedup_scale

        
