import pygame.font #for text

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, ai_settings, screen, stats): #report values it's tracking
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings for scoring information
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score image
        self.prep_score()

    def prep_score(self):
        """Turn score into rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.ai_settings.bg_colour)

        #Display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #20 px from right screen edge
        self.score_rect.top = 20 #20 px from top edge

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
