import sys
import pygame

#this allows you to condense and isolate the main event loop
#pygame.event.get() command is a collection of events that Pygame detects

def check_events():
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #program responds to key being pressed
        elif event.type == pygame.KEYDOWN:
            #check if key is right arrow key
            if event.key == pygame.K_RIGHT:
                #move mermaid to the right
                mermaid.moving_right = True
        #program then responds again when key is unpressed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #stop moving mermaid
                mermaid.moving_right = False

#update_screen function allows for further simplification of run_game
def update_screen(ai_settings, screen, mermaid):
    """Update images on screen and flip to new screen"""
    #redraw screen during each loop iteration
    screen.fill(ai_settings.bg_colour)
    mermaid.blitme()
    #tells pygame to display recently drawn screen
    pygame.display.flip()
