
##ALIEN INVASION 
#  IMAGE
#ship image
import pygame
from pygame.sprite import Sprite



class Branchbit(Sprite):
    def __init__(self,ai_settings,screen):
        '''initialize the ship and set its starting position'''
        self.screen = screen
        #callowing for decimal pixel movements
        self.ai_settings = ai_settings 
        
        #create a bullet react at (0,0) --> set correct position
        #self.rect = pygame.Rect(0, 0, ai_settings.bb_width, ai_settings.bb_height)
        #self.rect.centerx = ai_settings.bb_prev_locx
        #self.rect.top = ai_settings.bb_prev_locy
        
        ##store the bullet's position as a decimal value
        #self.y = float(self.rect.y)
        self.color = ai_settings.bb_color
        
        #self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        #self.image = pygame.image.load('images/ship.bmp')
        #self.rect = self.image.get_rect() #everything interpreted as rectangle 
        #self.screen_rect = screen.get_rect()
        
        #start each new ship at bottom center of the screen
        #NOTE: (0,0) is top-left corner of the screen...bottom-right corner of screen(1200,800) is (1200,800)
        #self.rect.centerx = self.screen_rect.centerx #center x-coordinate
        #self.rect.bottom = self.screen_rect.bottom #top,bottom,left,right
        
        ##store a decimal value for ship's center
        #self.center = float(self.rect.centerx)
        ##movement flags
        #self.moving_right = False
        #self.moving_left = False
        
    #def update(self):
        #'''update ship's position based on movement flag'''
        #if self.moving_right and self.rect.right<self.screen_rect.right:
            ##self.rect.centerx += 1
            #self.center += self.ai_settings.ship_speed_factor
        #if self.moving_left and self.rect.left>0:
            ##self.rect.centerx -= 1
            #self.center -= self.ai_settings.ship_speed_factor
        ##update rect object from self.center
        #self.rect.centerx = self.center
        
    def draw_bit(self,ai_settings,screen,ct_x,ct_y,swidth=None,sheight=None):
        self.screen = screen
        self.ai_settings = ai_settings 
        '''draw ship at its current location'''
        swidth = swidth if type(swidth)!=type(None) else ai_settings.bb_width
        sheight = sheight if type(sheight)!=type(None) else ai_settings.bb_height
        #self.screen.blit(self.image,self.rect) #draws image at position rect
        self.rect = pygame.Rect(0, 0, swidth,sheight)
        self.rect.centerx = ai_settings.bb_prev_locx - ct_x*ai_settings.bb_width/2
        self.rect.top = ai_settings.bb_prev_locy + ct_y*ai_settings.bb_height
        
        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    #def center_ship(self):
        #'''centers ship on screen'''
        #self.center = self.screen_rect.centerx

