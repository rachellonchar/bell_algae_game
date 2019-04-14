
##ALIEN INVASION 
#  IN-GAME FUNCTIONS/MOVEMENTS 
import sys
from time import sleep #pauses game when loss a life/ship
import pygame
import random 
import numpy as np

#from bullet import Bullet
#from alien import Alien
#from branch_bits import Branchbit

from alga import Alga
from swirl import Swirl1
from alga_group import Clump


#KEY EVENTS
#------------------------------------------------------------------------------
def check_key_events(event,ai_settings,stats,sb,screen,ship,bullets,press_direction):
    '''respond to keypresses'''
    
    #move left and right:
    if event.key == pygame.K_UP:
        ai_settings.update_eddy_size(20)
        #None
    elif event.key == pygame.K_DOWN:
        ai_settings.update_eddy_size(-20)
        #None
    
    #fire bullets
    elif press_direction=='down' and event.key==pygame.K_SPACE:
        ai_settings.initialize_dynamic_settings()
        #pygame.mouse.set_visible(False)
        
        #reset game stats
        stats.reset_stats()
        stats.game_active = False
        
        #reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        bullets.update()
        create_bloom(ai_settings,screen,bullets)
        update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)
    
    #quit game
    elif press_direction=='down' and event.key==pygame.K_q:
        sys.exit()
   
def check_play_button(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,mouse_x,mouse_y):
    '''start new game when player clicks play button'''
    #swirl = swirls[0]
    start_button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    swirl_click = screen_obj.rect.collidepoint(mouse_x,mouse_y)
    if start_button_clicked and not stats.game_active:
        #hide mouse cursur and reset game settings
        ai_settings.initialize_dynamic_settings()
        #pygame.mouse.set_visible(False)
        
        #reset game stats
        stats.reset_stats()
        stats.game_active = True
        
        #reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        bullets.update()
        create_bloom(ai_settings,screen,bullets)
        update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)

    elif swirl_click and stats.game_active:
        eddy = Swirl1(ai_settings,screen)
        eddy.reset_spin()
        eddy.update(ai_settings,mouse_x,mouse_y)
        eddies.add(eddy)
        update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)

def check_events(ai_settings, screen, stats, sb, play_button, eddies,screen_obj,bullets,congloms):
    '''respond to keypresses and mouse events'''
    #swirl = swirls[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_events(event,ai_settings,stats,sb,screen,eddies,bullets,'down')
        elif event.type == pygame.KEYUP:
            check_key_events(event,ai_settings,stats,sb,screen,eddies,bullets,'up')
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,mouse_x,mouse_y)

#----------
#ALGAE INTERACTIONS
#------------------------------------------------------------------------------
def check_eddies_collide(ai_settings,screen,stats,sb,eddies,bullets,congloms):
    '''update position of bullets and get rid of old bullets'''
    for bullet in bullets:
        for eddy in eddies:
            bullet.update_when_hit(eddy)
            #hit_bullets.add(bullet)
    

def check_effected_algae(ai_settings,screen,stats,sb,eddies,bullets,conglums):
    '''update position of bullets and get rid of old bullets'''
    
    for bullet in bullets:
        bullets_clumped = []
        for bullet2 in bullets:
            if bullet!=bullet2:
                clump_mark = bullet.bullets_in_range(bullet2)
                if clump_mark:
                    bullets_clumped.append(bullet2)

#----------
#CREATE ALGAE
#------------------------------------------------------------------------------
def create_alga(ai_settings,screen,bullets):
    alga = Alga(ai_settings,screen)
    place_x = random.randrange(10,ai_settings.screen_width-10,1)
    place_y = random.randrange(70,ai_settings.screen_height-10,1)
    
    alga.rect.x = place_x
    alga.rect.y = place_y
    alga.set_speed()
    bullets.add(alga)

def create_clump(ai_settings,screen,congloms,place_x,place_y,clump_size):
    clump = Clump(ai_settings,screen,clump_size)
    clump.rect.x = place_x
    clump.rect.y = place_y
    clump.set_speed()
    congloms.add(clump)

def create_bloom(ai_settings,screen,bullets,N=100):
    for ii in range(0,N):
        create_alga(ai_settings,screen,bullets)
        

#----------
#UPDATE SCREEN AND OBJECTS
#------------------------------------------------------------------------------

def update_bullets(ai_settings,screen,stats,sb,eddies,bullets,congloms):
    '''update position of bullets and get rid of old bullets'''
    bullets.update()
    congloms.update()

def update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms):
    '''update images on the screen and flip to next screen'''
    screen.fill(ai_settings.bg_color)
    screen_obj.draw_screen_top(ai_settings,screen)

    #eddies set to show_eddies when mouse click detected

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for clump in congloms.sprites():
        clump.draw_bullet()
    for eddy in eddies:
        if eddy.spins<4:
            eddy.update_rotate()
            eddy.blitme()
        else:
            eddies.empty()
    sb.show_score()
    
    check_eddies_collide(ai_settings,screen,stats,sb,eddies,bullets,congloms)
    check_effected_algae(ai_settings,screen,stats,sb,eddies,bullets,congloms)
    
    if not stats.game_active:
        play_button.draw_button() #draw after other elements so it appears on top
    pygame.display.flip() #updates the display

    
    
