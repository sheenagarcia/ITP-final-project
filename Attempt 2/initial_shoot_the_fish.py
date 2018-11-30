import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from mermaid import Mermaid
from fish import Fish
import game_functions as gf

#Initialize game
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shoot the Fish")

    #Load and play music
    pygame.mixer.music.load('theme_song_2.mid')
    pygame.mixer.music.play()

    #Make play button
    play_button = Button(ai_settings, screen, "Shoot the Fish!")

    #Create instance to store game statistics + scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    mermaid = Mermaid(ai_settings, screen) #Make a mermaid
    fishes = Group() #Make fish
    bubbles = Group() #Make group to store bubbles in; groups behave like lists, but have extra functionality

    #Create school of fish
    gf.create_school(ai_settings, screen, mermaid, fishes)

    #Start main loop
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, mermaid, fishes, bubbles)

        if stats.game_active:
            mermaid.update()
            gf.update_bubbles(ai_settings, screen, stats, sb, mermaid, fishes, bubbles)
            gf.update_fishes(ai_settings, stats, screen, sb, mermaid, fishes, bubbles)

        gf.update_screen(ai_settings, screen, stats, sb, mermaid, fishes, bubbles, play_button)

run_game()
