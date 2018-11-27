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

        #movement flag; set to false initially
        self.moving_right = False
        self.moving_left = False

    #however, we add the update function based on the mvt flag that will move the mermaid +1 to the right if True
    def update(self):
        """Update mermaid position based on mvt flag"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the mermaid at its current location"""
        self.screen.blit(self.image, self.rect)
