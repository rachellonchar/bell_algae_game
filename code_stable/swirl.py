
##ALIEN INVASION 
#  IMAGE
#ship image
import pygame
from pygame.sprite import Sprite



class Swirl1(Sprite):
    def __init__(self,ai_settings,screen):
        '''initialize the ship and set its starting position'''
        super().__init__()
        self.screen = screen
        #callowing for decimal pixel movements
        self.ai_settings = ai_settings 
        self.size = ai_settings.ed_size
        
        self.image = pygame.image.load('images/swirl_basic.bmp')
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        #self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect() #everything interpreted as rectangle 
        self.spins = 0 

    def update(self,ai_settings,mouse_x,mouse_y):
        self.size = ai_settings.ed_size
        self.image = pygame.transform.scale(self.image, (self.size,self.size))
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y
    def update_rotate(self):
        self.image = pygame.transform.rotate(self.image,90)
        self.spins += 1
    def reset_spin(self):
        self.spins = 0
        
    def blitme(self):
        '''draw ship at its current location'''
        #pygame.transform.rotate(self.image,45)
        self.screen.blit(self.image,self.rect) #draws image at position rect

    
