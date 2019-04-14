
from initiate import *
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

#def create_clump(ai_settings,screen,congloms,place_x,place_y,clump_size):
    #clump = Clump(ai_settings,screen,clump_size)
    #clump.rect.x = place_x
    #clump.rect.y = place_y
    #clump.set_speed()
    #congloms.add(clump)

def create_bloom(ai_settings,screen,bullets,N=350):
    for ii in range(0,N):
        create_alga(ai_settings,screen,bullets)

#----------
#UPDATE ALGAE
#------------------------------------------------------------------------------
def update_bullets(ai_settings,screen,stats,sb,eddies,bullets,congloms):
    '''update position of bullets and get rid of old bullets'''
    for bullet in bullets:
        bullet.update()
    #congloms.update()
