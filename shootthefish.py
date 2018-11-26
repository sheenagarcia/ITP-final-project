import sys
import pygame

from settings import Settings
from mermaid import Mermaid

#initialize game
def run_game():
    pygame.init()
    ai_settings = Settings()
    #create pygame "surface" = display game element
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #tuple defines screen dimensions
    pygame.display.set_caption("Shoot the Fish")
    bg_colour = (198, 180, 160) #RGB colours

    #Make ship
    mermaid = Mermaid(screen)

#The game is controlled by a while loop
    #event = user action
    #event loop = makes program wait & respond to user input
    while True:
        for event in pygame.event.get(): #pygame.event.get() command is a collection of events that Pygame detects
            if event.type == pygame.QUIT:
                sys.exit()
        #redraw screen during each loop iteration
        screen.fill(ai_settings.bg_colour)
        mermaid.blitme()
        #tells pygame to display recently drawn screen
        pygame.display.flip()




run_game()
