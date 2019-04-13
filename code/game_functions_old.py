
##ALIEN INVASION 
#  IN-GAME FUNCTIONS/MOVEMENTS 
import sys
from time import sleep #pauses game when loss a life/ship
import pygame
from bullet import Bullet
from alien import Alien
from branch_bits import Branchbit



def check_key_events(event,ai_settings,screen,ship,bullets,press_direction):
    '''respond to keypresses'''
    
    #move left and right:
    if event.key == pygame.K_RIGHT:
        #ship.moving_right = True if press_direction=='down' else False
        None
    elif event.key == pygame.K_LEFT:
        #ship.moving_left = True if press_direction=='down' else False
        None
    
    #fire bullets
    elif press_direction=='down' and event.key==pygame.K_SPACE:
        #fire_bullet(ai_settings,screen,ship,bullets)
        None
    
    #quit game
    elif press_direction=='down' and event.key==pygame.K_q:
        sys.exit()
   
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    '''start new game when player clicks play button'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
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
        
        #empty list of aliens and bullets
        aliens.empty()
        bullets.empty()
        
        #create new fleet and center ship
        #create_fleet(ai_settings,screen,ship,aliens)
        #ship.center_ship()

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    '''respond to keypresses and mouse events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            check_key_events(event,ai_settings,screen,ship,bullets,'down')
        elif event.type == pygame.KEYUP:
            check_key_events(event,ai_settings,screen,ship,bullets,'up')
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            
#def create_branch(ai_settings,screen,branches,last_branchx,last_branchy):
    ##create alien and place it in a row
    #branch = Branchbit(ai_settings,screen)
    #branch_width = branch.rect.width
    #branch.x = last_branchx - ct_x*ai_settings.bb_width/2
    #branch.rect.x = branch.x
    #branch.rect.y = last_branchy + ct_y*ai_settings.bb_height
    #branches.add(branch)

#def draw_main_branch(ai_settings,screen,branch):
    ##branch = Branchbit(ai_settings,screen)
    #ct_x = 0
    #ct_y = 0
    #branch.draw_bit(ai_settings,screen,ct_x,ct_y,swidth=6,sheight=10)
    
    #branch.draw_bit(ai_settings,screen,0,2,swidth=50,sheight=50)
    ##for ct_y in range(0,12):
        ##branch.draw_bit(ai_settings,screen,ct_x,ct_y)
        ##if ct_y>5:
            ##ct_x += 1

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,branch):
    '''update images on the screen and flip to next screen'''
    screen.fill(ai_settings.bg_color)
    
    #redraw all bullets behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
      
    #draw score info
    sb.show_score()
    
    ship.blitme()
    #antenna.blitme()
    aliens.draw(screen)
    #draw_main_branch(ai_settings,screen,branch)
    
    if not stats.game_active:
        play_button.draw_button() #draw after other elements so it appears on top
    pygame.display.flip() #updates the display

#def check_high_score(stats,sb):
    #'''check for new high score'''
    #if stats.score > stats.high_score:
        #stats.high_score = stats.score
        #sb.prep_high_score()
    
#def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #'''update position of bullets and get rid of old bullets'''
    #bullets.update()
    ##get rid of bullets that have disappeared
    #for bullet in bullets.copy():
        #if bullet.rect.bottom <= 0:
            #bullets.remove(bullet)
            
    ##check for bullets that have hit aliens
    #collisions = pygame.sprite.groupcollide(bullets,aliens,False,True) #true tells bullet/alien to dissapear
    #if collisions:
        #for aliens in collisions.values():
            #stats.score += ai_settings.alien_points*len(aliens)
            #sb.prep_score()
        #check_high_score(stats,sb)
    
    ##create new fleet when all aliens gone
    #if len(aliens)==0:
        ##if fleet destroyed, start new level
        #bullets.empty()
        #ai_settings.increase_speed()
        ##level up
        #stats.level += 1
        #sb.prep_level()
        #create_fleet(ai_settings,screen,ship,aliens)

#def fire_bullet(ai_settings,screen,ship,bullets):
    ##create new bullet and add it to the bullets group
    #if len(bullets) < ai_settings.bullets_allowed:
        #new_bullet = Bullet(ai_settings, screen, ship)
        #bullets.add(new_bullet)

#def change_fleet_direction(ai_settings,aliens):
    #for alien in aliens.sprites():
        #alien.rect.y += ai_settings.fleet_drop_speed
    #ai_settings.fleet_direction *= -1
    
#def check_fleet_edges(ai_settings,aliens):
    #for alien in aliens.sprites():
        #if alien.check_edges():
            #change_fleet_direction(ai_settings,aliens)
            #break
            
            
#def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    #'''update position of all aliens in the fleet'''
    #check_fleet_edges(ai_settings,aliens)
    #aliens.update()
    
    ##look for alien-ship collisions
    #if pygame.sprite.spritecollideany(ship,aliens):
        #ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    ##look for aliens hitting bottom of the screen
    #check_aliens_bottom(ai_settings,stats, screen,ship,aliens,bullets)


#def get_number_aliens_x(ai_settings,alien_width):
        ##determine number aliens in a row
        #available_space_x = ai_settings.screen_width - 2*alien_width
        #number_aliens_x = int(available_space_x/(2*alien_width))
        #return number_aliens_x
        
#def get_number_rows(ai_settings,ship_height,alien_height):
    #available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    #number_rows = int(available_space_y/(2*alien_height))-1
    #return number_rows
        
#def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    ##create alien and place it in a row
    #alien = Alien(ai_settings,screen)
    #alien_width = alien.rect.width
    #alien.x = alien_width + 2*alien_width*alien_number
    #alien.rect.x = alien.x
    #alien.rect.y = alien.rect.height*2 + 2*alien.rect.height*row_number
    #aliens.add(alien)

    
#def create_fleet(ai_settings,screen,ship,aliens):
    #'''create a full fleet of aliens'''
    #alien = Alien(ai_settings,screen)
    #number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    #number_rows = get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    
    ##create the fleet
    #for row_number in range(number_rows):
        #for alien_number in range(number_aliens_x):
            ##create alien and place in row
            #create_alien(ai_settings,screen,aliens,alien_number,row_number)


#def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    #'''respond to ship being hit by alien'''
    
    #if stats.ships_left > 0:
        #stats.ships_left -= 1
        #aliens.empty()
        #bullets.empty()
        ##create new fleet and center the ship
        #create_fleet(ai_settings,screen,ship,aliens)
        #ship.center_ship()
        ##pause
        #sleep(0.5)
    #else:
        #stats.game_active = False
        #pygame.mouse.set_visible(True)

#def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    #'''check if aliens hit bottom of screen'''
    #screen_rect = screen.get_rect()
    #for alien in aliens.sprites():
        #if alien.rect.bottom >= screen_rect.bottom:
            #ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            #break
    

    
    
    
    
    
    
    
