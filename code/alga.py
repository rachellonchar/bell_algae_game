
##ALIEN INVASION 
#  IMAGE/SPRITE
#bullet image
import pygame
from pygame.sprite import Sprite
import random 

#print(random.randrange(0,1000,1))
#print(random.randrange(0,700,1))



class Alga(Sprite):
    '''a class to manage bullets leaving the ship'''
    def __init__(self,ai_settings,screen):
        '''create bullet object a ship's current position'''
        super().__init__()
        self.screen = screen 
        
        self.screen_width = ai_settings.screen_width
        self.screen_height = ai_settings.screen_height
        
        #create a bullet react at (0,0) --> set correct position
        #self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.image = pygame.image.load('images/one_algae.bmp')
        self.image = pygame.transform.scale(self.image, (10,10))
        #self.image = pygame.transform.rotate(self.image,0)
        self.rect = self.image.get_rect() #
        
        #self.color = ai_settings.bullet_color
        self.bullet_speedx = ai_settings.bullet_speed_factor
        self.bullet_speedy = ai_settings.bullet_speed_factor
        #self.speedup_factor = ai_settings.temp_speedup
        #self.speed_factor = ai_settings.bullet_speed_factor 
        self.reset_speed = ai_settings.bullet_speed_factor
        self.felt_eddy = 0
        self.num_cells = 1
    
    def set_speed(self):
        fac_x = random.randrange(-1,2,2)
        self.bullet_speedx = fac_x*self.bullet_speedx
        
        fac_y = random.randrange(-1,2,2)
        self.bullet_speedy = fac_y*self.bullet_speedy
    
    def update(self):
        '''move bullet up the screen'''
        if self.rect.x == self.screen_width-10 or self.rect.x == 10:
            sign = 1 if self.bullet_speedx>0 else -1
            self.bullet_speedx = sign*self.reset_speed
        self.rect.x += self.bullet_speedx
            
        if self.rect.y == self.screen_height-10 or self.rect.y <= 10:
            sign = 1 if self.bullet_speedy>0 else -1
            self.bullet_speedy = sign*self.reset_speed
        self.rect.y += self.bullet_speedy
        
        if self.rect.x > self.screen_width or self.rect.x < 0:
            self.bullet_speedx = self.reset_speed*self.num_cells
            placex = random.randrange(-1,2,2)
            if placex==-1:
                self.rect.x = 11
            else:
                self.rect.x = self.screen_width - 11
        if self.rect.y > self.screen_height or self.rect.y < 0:
            self.bullet_speedy = self.reset_speed*self.num_cells
            placey = random.randrange(-1,2,2)
            if placey==-1:
                self.rect.y = 11
            else:
                self.rect.y = self.screen_height - 11
            
    def update_when_hit(self,eddy):#,hit_bullets):
        eddy_rect = eddy.rect
        if eddy_rect.contains(self.rect):
            self.felt_eddy = 1
            dirc_x = random.randrange(-1,2,2)
            dirc_y = random.randrange(-1,2,2)
            if dirc_x==-1:
                self.bullet_speedx = -1.1*abs(self.bullet_speedx)
            else:
                self.bullet_speedx = 1.1*abs(self.bullet_speedx)
            if dirc_y==-1:
                self.bullet_speedy = -1.1*abs(self.bullet_speedy)
            else:
                self.bullet_speedy = 1.1*abs(self.bullet_speedy)
    
    def draw_bullet(self):
        ##self.image = pygame.transform.rotate(self.image,45)
        self.screen.blit(self.image,self.rect) #draws image at position rect
        
    #def bullets_in_range(self,bullet2):
        #mark_to_clump = False
        #if self.felt_eddy>0 and bullet2.felt_eddy>0:
            #bul2_rec = bullet2.rect
            #rec_copy = bul2_rec.copy()
            #rec_copy.inflate_ip(500,500)
            #if rec_copy.contains(self.rect):
                ##self.image = pygame.image.load('images/one_algae.bmp')
                #mark_to_clump = True
        #return mark_to_clump
    def bullets_in_range(self,bullet2):
        mark_to_clump = False
        if self.felt_eddy>0 and bullet2.felt_eddy>0:
            bul2_rec = bullet2.rect
            rec_copy = bul2_rec.copy()
            rec_copy.inflate_ip(40,40)
            if rec_copy.contains(self.rect):
                #self.image = pygame.image.load('images/one_algae.bmp')
                self.rect.left = bul2_rec.right
                self.rect.top = bul2_rec.centery
            self.felt_eddy += 1
            mark_to_clump = True
        return mark_to_clump
            
        
        
    
    
