
##ALIEN INVASION 
#  MAIN FILE
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
#from alien import Alien
import game_functions as gf

#http://website.nbm-mnb.ca/mycologywebpages/NaturalHistoryOfFungi/AlgalMutualisms.html
#https://nph.onlinelibrary.wiley.com/doi/full/10.1111/j.1469-8137.2006.01792.x
#https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2745.12975
#https://www.jstor.org/stable/40511430?seq=1#page_scan_tab_contents


def run_game():
    #initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #create play button
    play_button = Button(ai_settings,screen,'PLAY')
    
    #create instance to store game stats and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    #make ship
    ship = Ship(ai_settings,screen)
    
    #make a group to store bullets
    bullets = Group()
    
    #make an alien
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #start the main loop of the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        

run_game()
