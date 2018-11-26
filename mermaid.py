import pygame

class Mermaid():
    def __init__(self, screen):
        """"Initialize mermaid and set its starting position"""
        self.screen = screen

        #Load mermaid image (image must be bmp format)
        self.image = pygame.image.load('images/STF_mermaid.bmp')
        #pygame sees images as rectangles
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position starts at bottom-center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the mermaid at its current location"""
        self.screen.blit(self.image, self.rect)
