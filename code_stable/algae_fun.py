
##ALIEN INVASION 
#  MAIN FILE
import pygame
from pygame.sprite import Group
from settings import Settings
from time import sleep

from game_stats import GameStats
from scoreboard import Scoreboard

from button import Button
from screen_object import ScreenObj
#from ship import Ship, Antenna
from swirl import Swirl1#,Swirl2,Swirl3,Swirl4,Swirl5,Swirl6,Swirl7,Swirl8,Swirl9
from alga import Alga
#from branch_bits import Branchbit
import game_functions as gf

#http://website.nbm-mnb.ca/mycologywebpages/NaturalHistoryOfFungi/AlgalMutualisms.html
#https://nph.onlinelibrary.wiley.com/doi/full/10.1111/j.1469-8137.2006.01792.x
#https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2745.12975
#https://www.jstor.org/stable/40511430?seq=1#page_scan_tab_contents
#


def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Algae Fun')
    
    #create play button
    play_button = Button(ai_settings,screen,'PLAY')
    
    #create instance to store game stats and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    screen_obj = ScreenObj(ai_settings,screen)
    bullets = Group()
    congloms = Group()
    eddies = Group()
    #start the main loop of the game
    gf.update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button,eddies,screen_obj,bullets,congloms)
        if stats.game_active:
            #ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,eddies,bullets,congloms)
            gf.update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)
            sleep(0.1)
        

run_game()
