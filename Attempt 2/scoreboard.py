import pygame.font #for text
from pygame.sprite import Group

from mermaid import Mermaid

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
        self.prep_level()
        self.prep_mermaids()

    def prep_mermaids(self):
        """Show how many lives are left"""
        self.mermaids = Group()
        for mermaid_number in range (self.stats.mermaids_left):
            mermaid = Mermaid(self.ai_settings, self.screen)
            mermaid.rect.x = 10 + mermaid_number * mermaid.rect.width
            mermaid.rect.y = 10
            self.mermaids.add(mermaid)

    def prep_score(self):
        """Turn score into rendered image"""
        rounded_score = round(self.stats.score, -1) #round to nearest 10, 100, 1000, etc
        score_str = "{:,}".format(rounded_score) #string formating = insert commas into numbers
        self.score_image = self.font.render(score_str, True, self.text_colour, self.ai_settings.bg_colour)

        #Display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 #20 px from right screen edge
        self.score_rect.top = 20 #20 px from top edge

    def prep_level(self):
        """Turn the level into rendered image"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_colour, self.ai_settings.bg_colour)

        #Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 #position below score + 10 pixels

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #Draw mermaids
        self.mermaids.draw(self.screen)
