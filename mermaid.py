import pygame

class Mermaid():
    def __init__(self, screen):
        """"Initialize mermaid and set its starting position"""
        self.screen = screen
        #control speed via Settings
        self.ai_settings = ai_settings

        #Load mermaid image (image must be bmp format)
        self.image = pygame.image.load('images/STF_mermaid.bmp')
        #pygame sees images as rectangles
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position starts at bottom-center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #I used a float since I want the value to be a decimal number
        self.center = float(self.rect.centerx)

        #movement flag; set to false initially
        self.moving_right = False
        self.moving_left = False

    #however, we add the update function based on the mvt flag that will move the mermaid +1 to the right if True
    def update(self):
        """Update mermaid position based on mvt flag"""
        #I changed it to make the update based on mermaid's center value and not the rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #*then* I can update the rect from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the mermaid at its current location"""
        self.screen.blit(self.image, self.rect)
