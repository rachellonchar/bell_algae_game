
##ALIEN INVASION 
#  IMAGE/SPRITE
#bullet image
import pygame
from pygame.sprite import Sprite
import random 

print(random.randrange(0,1000,1))
print(random.randrange(0,700,1))



class Bullet(Sprite):
    '''a class to manage bullets leaving the ship'''
    def __init__(self,ai_settings,screen,ship):
        '''create bullet object a ship's current position'''
        super().__init__()
        self.screen = screen 
        
        #create a bullet react at (0,0) --> set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor 
    
    def update(self):
        '''move bullet up the screen'''
        self.y -= self.speed_factor 
        #update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        '''draw the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)