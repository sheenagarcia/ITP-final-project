import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from mermaid import Mermaid
import game_functions as gf

#Initialize game
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shoot the Fish")

    #Make a mermaid
    mermaid = Mermaid(ai_settings, screen)
    #Make group to store bubbles in
    bubbles = Group() #groups behave like lists, but have extra functionality

    #Start main loop
    while True:
        gf.check_events(ai_settings, screen, mermaid, bubbles)
        mermaid.update()
        gf.update_bubbles(bubbles)
        bubbles.update()
        gf.update_screen(ai_settings, screen, mermaid, bubbles)

run_game()
