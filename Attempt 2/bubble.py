import pygame
from pygame.sprite import Sprite

class Bubble (Sprite):
    """A class to manage bubbles fired from mermaid"""

    def __init__ (self, ai_settings, screen, mermaid):
        """Create bubble object at mermaid's current location"""
        super().__init__()
        self.screen = screen

        #Create bubble rect at (0,0) then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bubble_width, ai_settings.bubble_height)
        self.rect.centerx = mermaid.rect.centerx #make bubble's centerx the same as the mermaid
        self.rect.top = mermaid.rect.top #makes it look like the bubble fired from top of mermaid

        #Store bubble position as decimal value
        self.y = float(self.rect.y)

        self.colour = ai_settings.bubble_colour
        self.speed_factor = ai_settings.bubble_speed_factor

    def update(self):
        """Move bubble up the screen"""
        #Update decimal position of bubbles
        self.y -= self.speed_factor
        #Update rect position
        self.rect.y = self.y

    def draw_bubble(self):
        """Draw bubble to screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
