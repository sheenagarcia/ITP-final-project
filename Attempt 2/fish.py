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

    def blitme(self):
        """Draw fish at current location"""
        self.screen.blit(self.image, self.rect)
