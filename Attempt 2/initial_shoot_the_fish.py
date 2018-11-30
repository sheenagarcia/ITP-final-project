import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from mermaid import Mermaid
from fish import Fish
import game_functions as gf

#Initialize game
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shoot the Fish")

    #Create instance to store game statistics
    stats = GameStats(ai_settings)


    mermaid = Mermaid(ai_settings, screen) #Make a mermaid
    fishes = Group() #Make fish
    bubbles = Group() #Make group to store bubbles in; groups behave like lists, but have extra functionality

    #Create school of fish
    gf.create_school(ai_settings, screen, mermaid, fishes)


    #Start main loop
    while True:
        gf.check_events(ai_settings, screen, mermaid, bubbles)
        mermaid.update()
        gf.update_bubbles(ai_settings, screen, mermaid, fishes, bubbles)
        gf.update_fishes(ai_settings, stats, screen, mermaid, fishes, bubbles)
        gf.update_screen(ai_settings, screen, mermaid, fishes, bubbles)

run_game()
