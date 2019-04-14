
##ALIEN INVASION 
#  IMAGE
#ship image
import pygame
#from pygame.sprite import Sprite



class ScreenObj():
    def __init__(self,ai_settings,screen):
        '''initialize the ship and set its starting position'''
        self.screen = screen
        #callowing for decimal pixel movements
        self.ai_settings = ai_settings 
        self.color = ai_settings.bg_color
        
    def draw_screen_top(self,ai_settings,screen):#,ct_x,ct_y,swidth=None,sheight=None):
        self.screen = screen
        self.ai_settings = ai_settings 
        '''draw ship at its current location'''
        swidth = ai_settings.screen_width
        sheight = ai_settings.screen_height

        self.rect = pygame.Rect(0, 0, swidth,sheight)
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        pygame.draw.rect(self.screen, self.color, self.rect)
    

