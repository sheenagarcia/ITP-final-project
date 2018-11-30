import pygame
from pygame.sprite import Sprite

class Fish(Sprite):
    def __init__(self, ai_settings, screen):
        """This class represents one fish"""
        super(Fish, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load fish and set its rectangle
        self.image = pygame.image.load('images/magikarp.bmp')
        self.rect = self.image.get_rect()

        #Start at top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Decimal to store position
        self.x = float(self.rect.x)

    #check to see if a fish hit the edge of the screen so it doesn't just fly off the screen
    def check_edges(self):
        """Return True if fish is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move fish left or right"""
        self.x += self.ai_settings.fish_speed_factor * self.ai_settings.school_direction
        self.rect.x = self.x

    def blitme(self):
        """Draw fish at current location"""
        self.screen.blit(self.image, self.rect)
