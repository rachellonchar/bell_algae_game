
##ALIEN INVASION 
#  IMAGE
#ship image
import pygame



class Ship():
    def __init__(self,ai_settings,screen):
        '''initialize the ship and set its starting position'''
        self.screen = screen
        #callowing for decimal pixel movements
        self.ai_settings = ai_settings 
        
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect() #everything interpreted as rectangle 
        self.screen_rect = screen.get_rect()
        
        #start each new ship at bottom center of the screen
        #NOTE: (0,0) is top-left corner of the screen...bottom-right corner of screen(1200,800) is (1200,800)
        self.rect.centerx = self.screen_rect.centerx #center x-coordinate
        self.rect.bottom = self.screen_rect.bottom #top,bottom,left,right
        
        #store a decimal value for ship's center
        self.center = float(self.rect.centerx)
        #movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''update ship's position based on movement flag'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        #update rect object from self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        '''draw ship at its current location'''
        #pygame.transform.rotate(self.image,45)
        self.screen.blit(self.image,self.rect) #draws image at position rect
    
    def center_ship(self):
        '''centers ship on screen'''
        self.center = self.screen_rect.centerx

class Antenna():
    def __init__(self,ai_settings,screen,ship):
        '''initialize the ship and set its starting position'''
        self.screen = screen
        #allowing for decimal pixel movements
        self.ai_settings = ai_settings 
        
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect() #everything interpreted as rectangle 
        #self.screen_rect = screen.get_rect()
        
        self.ship_rect = ship.rect
        
        #self.rect.centerx = self.screen_rect.centerx #center x-coordinate
        #self.rect.bottom = self.screen_rect.bottom #top,bottom,left,right
        
        self.rect.centerx = self.ship_rect.centerx
        self.rect.bottom = self.ship_rect.top
        
        #store a decimal value for ship's center
        self.center = float(self.rect.centerx)
        #movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        '''update ship's position based on movement flag'''
        if self.moving_right and self.rect.right<self.screen_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            #self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        #update rect object from self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        '''draw ship at its current location'''
        #pygame.transform.rotate(self.image,45)
        self.screen.blit(self.image,self.rect) #draws image at position rect
    
    def center_ant(self):
        '''centers ship on screen'''
        self.center = self.screen_rect.centerx

