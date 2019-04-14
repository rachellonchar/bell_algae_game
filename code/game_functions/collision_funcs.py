
from initiate import *
#from key_funcs import *

#----------
#ALGAE INTERACTIONS
#------------------------------------------------------------------------------
def check_eddies_collide(ai_settings,screen,stats,sb,eddies,bullets,congloms):
    '''update position of bullets and get rid of old bullets'''
    #None
    for bullet in bullets:
        for eddy in eddies:
            bullet.update_when_hit(eddy)
            #hit_bullets.add(bullet)
    

def check_effected_algae(ai_settings,screen,stats,sb,eddies,bullets,conglums):
    '''update position of bullets and get rid of old bullets'''
    
    #None
    for bullet in bullets:
        #bullets_clumped = []
        for bullet2 in bullets:
            if bullet!=bullet2:
                bullet.bullets_in_range(bullet2,ai_settings,stats)
    
