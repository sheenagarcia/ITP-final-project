import pygame

class Mermaid():
    def __init__(self, ai_settings, screen):
        """Initialize mermaid and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load mermaid and get its recently
        self.image = pygame.image.load('images/mermaid.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        #Start each new mermaid at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for mermaid's centre
        self.center = float(self.rect.centerx)

    def update(self):
        """Update mermaid position based on mvt flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.mermaid_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.mermaid_speed_factor

        #Update rect from center value
        self.rect.centerx = self.center

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_mermaid(self):
        """Center mermaid on screen"""
        self.center = self.screen_rect.centerx
