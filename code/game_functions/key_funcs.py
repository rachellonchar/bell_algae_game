
from initiate import *
from game_stats import GameStats
from scoreboard import Scoreboard
from create_class_images import *
from collision_funcs import *
#----------
#UPDATE SCREEN
#------------------------------------------------------------------------------
def update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms):
    '''update images on the screen and flip to next screen'''
    screen.fill(ai_settings.bg_color)
    screen_obj.draw_screen_top(ai_settings,screen)

    #eddies set to show_eddies when mouse click detected

    for bullet in bullets.sprites():
        if bullet.since_hit==0:
            None
        elif bullet.since_hit==1:
            bullet.algae_reset_speed(ai_settings)
        else:
            bullet.slowing()
        #bullet.update()
        bullet.draw_bullet()
        
    for eddy in eddies:
        if eddy.spins<4:
            eddy.update_rotate()
            eddy.blitme()
        else:
            eddies.empty()
            cursor = pygame.cursors.load_xbm(img_path+'stick.xbm',img_path+'stick-mask.xbm')
            pygame.mouse.set_cursor(*cursor)
    #stats = GameStats(ai_settings)
    sb.show_score()
    
    check_eddies_collide(ai_settings,screen,stats,sb,eddies,bullets,congloms)
    check_effected_algae(ai_settings,screen,stats,sb,eddies,bullets,congloms)
    
    if not stats.game_active:
        play_button.draw_button() #draw after other elements so it appears on top
    pygame.display.flip() #updates the display

#----------
#KEY EVENTS
#------------------------------------------------------------------------------
def check_key_events(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,event,press_direction):
    '''respond to keypresses'''
    
    #move left and right:
    if event.key == pygame.K_UP:
        if ai_settings.ed_size<1000:
            ai_settings.update_eddy_size(20)
        #None
    elif event.key == pygame.K_DOWN:
        if ai_settings.ed_size>20:
            ai_settings.update_eddy_size(-20)
        #None
    
    #fire bullets
    elif press_direction=='down' and event.key==pygame.K_SPACE:
        ai_settings.initialize_dynamic_settings()
        bullets.empty()
        stats.game_active = False
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
        cursor = pygame.cursors.load_xbm(img_path+'stick.xbm',img_path+'stick-mask.xbm')
        pygame.mouse.set_cursor(*cursor)
        stats.reset_stats()
        stats.game_active = True
        #reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        bullets.update()
        create_bloom(ai_settings,screen,bullets)
        #stats = GameStats(ai_settings)
        #sb.show_score()
        update_screen(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms)

    elif swirl_click and stats.game_active:
        cursor = pygame.cursors.load_xbm(img_path+'stick_dip.xbm',img_path+'stick_dip-mask.xbm')
        pygame.mouse.set_cursor(*cursor)
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
            bullets.empty()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_events(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,event,'down')
        elif event.type == pygame.KEYUP:
            check_key_events(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,event,'up')
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,eddies,screen_obj,bullets,congloms,mouse_x,mouse_y)
