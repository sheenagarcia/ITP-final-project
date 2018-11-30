import sys
import pygame
from bubble import Bubble
from fish import Fish

def get_number_rows(ai_settings, mermaid_height, fish_height):
    """Determine the number of rows of fish that fit on screen."""
    available_space_y = (ai_settings.screen_height - (3*fish_height) - mermaid_height)
    number_rows = int(available_space_y / (2 * fish_height))
    return number_rows

def get_number_fishes_x(ai_settings, fish_width):
    """Determine number of fish that fit in row"""
    available_space_x = ai_settings.screen_width - 2 * fish_width #margin = 1 fish width; two margins
    number_fishes_x = int(available_space_x / (2 * fish_width)) #space needed for 1 fish = 2x width of 1
    return number_fishes_x

def create_fish(ai_settings, screen, fishes, fish_number, row_number):
    """Create fish and place it in row"""
    #Create fish and place it in row
    fish = Fish(ai_settings, screen)
    fish_width = fish.rect.width
    fish.x = fish_width + 2 * fish_width * fish_number
    fish.rect.x = fish.x
    fish.rect.y = fish.rect.height + 2 * fish.rect.height * row_number
    fishes.add(fish)

def create_school(ai_settings, screen, mermaid, fishes):
    """Create school of fish"""
    #Create fish + find number of fish that fit in one row
    #Spacing between fish = 1 fish width
    fish = Fish(ai_settings, screen)
    number_fishes_x = get_number_fishes_x(ai_settings, fish.rect.width)
    number_rows = get_number_rows(ai_settings, mermaid.rect.height, fish.rect.height)

    #Create school of fish
    for row_number in range(number_rows):
        for fish_number in range(number_fishes_x):
            create_fish(ai_settings, screen, fishes, fish_number, row_number)

def check_school_edges(ai_settings, fishes):
    """Respond if fish reach edge"""
    for fish in fishes.sprites():
        if fish.check_edges():
            change_school_direction(ai_settings, fishes)
            break

def change_school_direction(ai_settings, fishes):
    """Drop fish and change fish direction"""
    for fish in fishes.sprites():
        fish.rect.y += ai_settings.school_drop_speed
    ai_settings.school_direction *= -1

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

def update_screen(ai_settings, screen, mermaid, fishes, bubbles):
    """Update images on screen and flip to new screen"""
    #Redraw screen during each loop iteration
    screen.fill(ai_settings.bg_colour)
    #Bubbles go behind fish and mermaid
    for bubble in bubbles.sprites():
        bubble.draw_bubble()
    mermaid.blitme()
    fishes.draw(screen) #using draw() on a group causes pygame to automatically draw each element in group to rect position

    #Make most recently drawn screen visible
    pygame.display.flip()

def update_bubbles(fishes, bubbles):
    """Update position of bubbles and get rid of old bubbles"""
        #Update bubble positions
    bubbles.update()
    #Get rid of bubbles that go off the screen
    for bubble in bubbles.copy():
        if bubble.rect.bottom <= 0:
            bubbles.remove(bubble)
    #print(len(bubbles)) you can see the output in terminal
    #Check for any bubbles that hit fish --> get rid of bubble + fish
    collisions = pygame.sprite.groupcollide(bubbles, fishes, True, True)

def update_fishes(ai_settings, fishes):
    """Check if school is at edge, then update positions of all fishes in school"""
    check_school_edges(ai_settings, fishes)
    fishes.update()
