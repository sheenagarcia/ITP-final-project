import sys
import pygame
from bubble import Bubble

def check_keydown_events(event, ai_settings, screen, mermaid, bubbles):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        mermaid.moving_right = True
    elif event.key == pygame.K_LEFT:
        mermaid.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bubble(ai_settings, screen, mermaid, bubbles)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bubble(ai_settings, screen, mermaid, bubbles):
    """Fire bubble if limit not reached yet"""
    #Create new bubble and add it to bubble group
    if len(bubbles) < ai_settings.bubbles_allowed: #makes it so only three bubbles can be on the screen at a time
        new_bubble = Bubble(ai_settings, screen, mermaid)
        bubbles.add(new_bubble)

def check_keyup_events (event, mermaid):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        mermaid.moving_right = False
    elif event.key == pygame.K_LEFT:
        mermaid.moving_left = False


def check_events(ai_settings, screen, mermaid, bubbles):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, mermaid, bubbles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mermaid)

def update_screen(ai_settings, screen, mermaid, bubbles):
    """Update images on screen and flip to new screen"""
    #Redraw screen during each loop iteration
    screen.fill(ai_settings.bg_colour)
    #Bubbles go behind fish and mermaid
    for bubble in bubbles.sprites():
        bubble.draw_bubble()
    mermaid.blitme()

    #Make most recently drawn screen visible
    pygame.display.flip()

def update_bubbles(bubbles):
    """Update position of bubbles and get rid of old bubbles"""
        #Update bubble positions
    bubbles.update()
    #Get rid of bubbles that go off the screen
    for bubble in bubbles.copy():
        if bubble.rect.bottom <= 0:
            bubbles.remove(bubble)
    #print(len(bubbles)) you can see the output in terminal
