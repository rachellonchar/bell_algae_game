
##ALIEN INVASION 
#  IMAGE
#alien image
import pygame
from pygame.sprite import Sprite



class Alien(Sprite):
    '''a class represent a single alien in the fleet'''
    
    def __init__(self,ai_settings,screen):
        '''initialize the alien and set its starting position'''
        super(Alien,self).__init__()
        self.screen = screen
        #callowing for decimal pixel movements
        self.ai_settings = ai_settings 
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() #everything interpreted as rectangle 
        
        #start each alien near the top-left of screen
        self.rect.x = self.rect.width #center x-coordinate
        self.rect.y = self.rect.height #top,bottom,left,right
        
        #store alien's exact position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        '''return true if alien is at edge of screen'''
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= 0:
            return True
        
    #alien movement
    def update(self):
        '''move the alien right'''
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def blitme(self):
        '''draw alien at its current location'''
        self.screen.blit(self.image,self.rect) #draws image at position rect
    
    

