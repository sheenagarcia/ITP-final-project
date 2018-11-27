import pygame

from settings import Settings
from mermaid import Mermaid
import game_functions as gf

#initialize game
def run_game():
    pygame.init()
    ai_settings = Settings()
    #create pygame "surface" = display game element
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #tuple defines screen dimensions
    pygame.display.set_caption("Shoot the Fish")
    bg_colour = (198, 180, 160) #RGB colours

    #Make mermaid
    mermaid = Mermaid(screen)

    #event = user action
    while True:
        gf.check_events(mermaid) #event loop = makes program wait & respond to user input
        ship.update()
        gf.update_screen(ai_settings, screen, mermaid)






run_game()
