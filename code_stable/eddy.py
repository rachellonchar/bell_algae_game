
##ALIEN INVASION 
#  IMAGE/SPRITE
#bullet image
import pygame
from pygame.sprite import Sprite
#import random 

#print(random.randrange(0,1000,1))
#print(random.randrange(0,700,1))



class Eddy(Sprite):
    '''a class to manage bullets leaving the ship'''
    def __init__(self,ai_settings,screen):
        '''create bullet object a ship's current position'''
        super().__init__()
        self.screen = screen 
        
        self.screen_width = ai_settings.screen_width
        self.screen_height = ai_settings.screen_height
        
        self.rect = pygame.Rect(0, 0, ai_settings.ed_px_width, ai_settings.ed_px_height)
        self.color = ai_settings.eddy_color
        self.ed_speedx = ai_settings.ed_speed_factor
        self.ed_speedy = ai_settings.ed_speed_factor 
    
    #def set_speed(self):
        #fac_x = random.randrange(-1,2,2)
        #self.bullet_speedx = fac_x*self.bullet_speedx
        
        #fac_y = random.randrange(-1,2,2)
        #self.bullet_speedy = fac_y*self.bullet_speedy
        
    def update(self,place_x,place_y):
        self.rect.centerx = place_x
        self.rect.centery = place_y
    
    #def update(self):
        #'''move bullet up the screen'''
        #if self.rect.x == self.screen_width-10 or self.rect.x == 10:
            #self.bullet_speedx = -1*self.bullet_speedx
        #self.rect.x += self.bullet_speedx
            
        #if self.rect.y == self.screen_height-10 or self.rect.y <= 10:
            #self.bullet_speedy = -1*self.bullet_speedy
        #self.rect.y += self.bullet_speedy

    def draw_pix(self):
        '''draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)
