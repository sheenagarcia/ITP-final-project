import sys
import pygame

def check_events(mermaid):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mermaid.moving_right = True
            if event.key == pygame.K_LEFT:
                mermaid.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mermaid.moving_right = False
            if event.key == pygame.K_LEFT:
                mermaid.moving_left = False

def update_screen(ai_settings, screen, mermaid):
    """Update images on screen and flip to new screen"""
    #Redraw screen during each loop iteration
    screen.fill(ai_settings.bg_colour)
    mermaid.blitme()

    #Make most recently drawn screen visible
    pygame.display.flip()
