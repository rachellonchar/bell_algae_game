
###ALIEN INVASION 
##  IMAGE/SPRITE
##bullet image
#import pygame
#from pygame.sprite import Sprite
#import random 

##print(random.randrange(0,1000,1))
##print(random.randrange(0,700,1))



#class Clump(Sprite):
    #'''a class to manage bullets leaving the ship'''
    #def __init__(self,ai_settings,screen,number_cells):
        #'''create bullet object a ship's current position'''
        #super().__init__()
        #self.screen = screen 
        
        #self.screen_width = ai_settings.screen_width
        #self.screen_height = ai_settings.screen_height
        
        #self.image = pygame.transform.scale(self.image, (10*number_cells,10*number_cells))
        #self.rect = self.image.get_rect() #
        
        #self.bullet_speedx = ai_settings.bullet_speed_factor*number_cells
        #self.bullet_speedy = ai_settings.bullet_speed_factor*number_cells
        ##self.speed_factor = ai_settings.bullet_speed_factor 
        #self.reset_speed = ai_settings.bullet_speed_factor*number_cells
        #self.felt_eddy = number_cells
        #self.num_cells = number_cells
        
        #self.since_hit = 0
    
    #def set_speed(self):
        #fac_x = random.randrange(-1,2,2)
        #self.bullet_speedx = fac_x*self.bullet_speedx
        
        #fac_y = random.randrange(-1,2,2)
        #self.bullet_speedy = fac_y*self.bullet_speedy
    
    #def update(self):
        #'''move bullet up the screen'''
        #if self.rect.x == self.screen_width-10 or self.rect.x == 10:
            #sign = 1 if self.bullet_speedx>0 else -1
            #self.bullet_speedx = sign*self.reset_speed*self.num_cells
        #self.rect.x += self.bullet_speedx
            
        #if self.rect.y == self.screen_height-10 or self.rect.y <= 10:
            #sign = 1 if self.bullet_speedy>0 else -1
            #self.bullet_speedy = sign*self.reset_speed*self.num_cells
        #self.rect.y += self.bullet_speedy
        
        #if self.rect.x > self.screen_width or self.rect.x < 0:
            #self.bullet_speedx = self.reset_speed*self.num_cells
            #placex = random.randrange(-1,2,2)
            #if placex==-1:
                #self.rect.x = 11
            #else:
                #self.rect.x = self.screen_width - 11
        #if self.rect.y > self.screen_height or self.rect.y < 0:
            #self.bullet_speedy = self.reset_speed*self.num_cells
            #placey = random.randrange(-1,2,2)
            #if placey==-1:
                #self.rect.y = 11
            #else:
                #self.rect.y = self.screen_height - 11
    
    #def draw_bullet(self):
        ###self.image = pygame.transform.rotate(self.image,45)
        #self.screen.blit(self.image,self.rect) #draws image at position rect
        
    #def bullets_in_range(self,bullet2):
        #mark_to_clump = False
        #if self.felt_eddy>0 and bullet2.felt_eddy>0:
            #bul2_rec = bullet2.rect
            #rec_copy = bul2_rec.copy()
            #rec_copy.inflate_ip(2,2)
            #if rec_copy.contains(self.rect):
                ##self.image = pygame.image.load('images/one_algae.bmp')
                #self.rect.left = bul2_rec.right
                #self.rect.top = bul2_rec.centery
    
    #def update_when_hit(self,eddy):#,hit_bullets):
        #eddy_rect = eddy.rect
        #if eddy_rect.contains(self.rect):
            #self.felt_eddy = 1
            #self.locate_quad(eddy)
            #self.bullet_speedx = 1.1*self.bullet_speedx
            #self.bullet_speedy = 1.1*self.bullet_speedy
            #self.since_hit = 10
    #def slowing(self):
        #self.since_hit -= 1
    
    #def algae_reset_speed(self,ai_settings):
        #if self.bullet_speedx>0:
            #dircx = 1
        #else:
            #dircx = -1
        #if self.bullet_speedy>0:
            #dircy = 1
        #else:
            #dircy = -1
        #self.bullet_speedy = dircy*ai_settings.reset_speed
        #self.bullet_speedx = dircx*ai_settings.reset_speed
        #self.since_hit = 0
    
    #def locate_quad(self,eddy):
        #'''which quadrant of the eddy is the algae in'''
        #bt,bb = eddy.rect.top,eddy.rect.bottom
        #bl,br = eddy.rect.left,eddy.rect.right
        
        #sx,sy = self.rect.centerx,self.rect.centery
        
        #if abs(bl-sx)>abs(br-sx):
            ##closer to the right, 1 or 4
            #tendx = [1,4]
        #else:
            #tendx = [2,3]
        #if abs(bt-sy)>abs(bb-sy):
            ##closer to the bottom 
            #quad = tendx[1]
        #else:
            #quad = tendx[0]
        
        ##x,y directions
        #if quad in [2,1]:
            #self.bullet_speedx = abs(self.bullet_speedx)
        #else:
            #self.bullet_speedx = -1*abs(self.bullet_speedx)
        #if quad in [2,3]:
            #self.bullet_speedy = abs(self.bullet_speedy)
        #else:
            #self.bullet_speedy = -1*abs(self.bullet_speedy)

            
        
        
    
    
