
##ALIEN INVASION 
#  IMAGE/SPRITE
#bullet image

#----------
import pygame
from pygame.sprite import Sprite
import random 

#regular code directory setup:
import sys, os, os.path
cwd = os.getcwd()
main_dirc = cwd.split('bell_algae_game', 1)[0]
img_path = main_dirc+'/bell_algae_game/images/'



class Alga(Sprite):
    '''a class to manage un-conglomorated algae cells'''
    def __init__(self,ai_settings,screen):
        '''create algae in random locations'''
        super().__init__()
        self.screen = screen 
        
        self.screen_width = ai_settings.screen_width
        self.screen_height = ai_settings.screen_height
        
        self.image = pygame.image.load(img_path+'one_algae.bmp')
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect() #
        
        self.bullet_speedx = ai_settings.bullet_speed_factor
        self.bullet_speedy = ai_settings.bullet_speed_factor

        self.reset_speed = ai_settings.bullet_speed_factor
        self.felt_eddy = 0
        self.num_cells = 1
        self.update_frames = 0
        
        self.since_hit = 0
        self.last_in_chain = False
        self.first_in_chain = False
        self.in_chain = False
    
    def set_speed(self):
        fac_x = random.randrange(-1,2,2)
        new_speedx = fac_x*self.bullet_speedx
        self.bullet_speedx = new_speedx
        
        fac_y = random.randrange(-1,2,2)
        new_speedy = fac_y*self.bullet_speedy
        self.bullet_speedy = new_speedy
        
        #print(fac_x,fac_y)
        #print(self.bullet_speedx,self.bullet_speedy)
        #print(self.rect.x,self.rect.y)
        #print(' ')
    
    def update(self):
        '''move bullet up the screen'''
        self.rect.x += self.bullet_speedx
        self.rect.y += self.bullet_speedy
        
        if self.rect.x > self.screen_width-3 or self.rect.x < 3:
            if self.rect.x < 3 and self.bullet_speedx < 0:
                self.rect.x = self.screen_width-5
            elif self.rect.x > self.screen_width-10 and self.bullet_speedx > 0:
                self.rect.x = 14
        if self.rect.y > self.screen_height-10 or self.rect.y < 10:
            if self.rect.y < 10 and self.bullet_speedy < 0:
                self.rect.y = self.screen_height-14
            if self.rect.y < self.screen_height-10 and self.bullet_speedy > 0:
                self.rect.y = 14
        
        #print(self.rect.x,self.rect.y)
        #if self.in_chain==True:
            #self.update_frames += 1
            #if 
            
            
    def update_when_hit(self,eddy):#,hit_bullets):
        
        eddy_rect = eddy.rect
        #nmsp = 1.6
        if eddy.size==200:
            speed_up = 2
        elif eddy.size>200 and eddy.size<280:
            speed_up = 2
        elif eddy.size>=280:
            speed_up = 3
        elif eddy.size<200 and eddy.size>120:
            speed_up = 2
        elif eddy.size<=120:
            speed_up = 1
        #speed_up = 3
        if eddy_rect.contains(self.rect):
            self.felt_eddy = 1
            self.locate_quad(eddy)
            self.bullet_speedx = speed_up*self.bullet_speedx
            self.bullet_speedy = speed_up*self.bullet_speedy
            self.since_hit = 6
        
    def slowing(self):
        #signx = 1 if self.bullet_speedx>0 else -1
        #signy = 1 if self.bullet_speedy>0 else -1
        if self.bullet_speedx>1:
            self.bullet_speedx -= 1
        elif self.bullet_speedx<-1:
            self.bullet_speedx += 1
        if self.bullet_speedy>1:
            self.bullet_speedy -= 1
        elif self.bullet_speedy<-1:
            self.bullet_speedy += 1
        self.since_hit -= 1
    
    def algae_reset_speed(self,ai_settings):
        if self.bullet_speedx>0:
            dircx = 1
        else:
            dircx = -1
        if self.bullet_speedy>0:
            dircy = 1
        else:
            dircy = -1
        self.bullet_speedy = dircy*self.reset_speed
        self.bullet_speedx = dircx*self.reset_speed
        #print(self.reset_speed,'(',self.rect.x,self.rect.y,')')
        self.since_hit = 0
    
    def locate_quad(self,eddy):
        '''which quadrant of the eddy is the algae in'''
        bt,bb = eddy.rect.top,eddy.rect.bottom
        bl,br = eddy.rect.left,eddy.rect.right
        
        sx,sy = self.rect.centerx,self.rect.centery
        
        if abs(bl-sx)>abs(br-sx):
            #closer to the right, 1 or 4
            tendx = [1,4]
        else:
            tendx = [2,3]
        if abs(bt-sy)>abs(bb-sy):
            #closer to the bottom 
            quad = tendx[1]
        else:
            quad = tendx[0]
        
        #x,y directions
        if quad in [2,1]:
            self.bullet_speedx = abs(self.bullet_speedx)
        else:
            self.bullet_speedx = -1*abs(self.bullet_speedx)
        if quad in [2,3]:
            self.bullet_speedy = abs(self.bullet_speedy)
        else:
            self.bullet_speedy = -1*abs(self.bullet_speedy)
        
        if abs(bl-sx)<20 or abs(br-sx)<20:
            #closer to the right, 1 or 4
            self.bullet_speedy += self.bullet_speedy
        if abs(bt-sy)<20 or abs(bb-sy)<20:
            #closer to the bottom 
            self.bullet_speedx += self.bullet_speedx
    
    def draw_bullet(self):
        ##self.image = pygame.transform.rotate(self.image,45)
        self.screen.blit(self.image,self.rect) #draws image at position rect
        
    def bullets_in_range(self,bullet2,ai_settings,stats):
        #None
        bul2_rec = bullet2.rect
        rec_copy = bul2_rec.copy()
        rec_copy.inflate_ip(15,15) #pixel area of sticking range
        if rec_copy.contains(self.rect):
            if bullet2.in_chain==False or bullet2.last_in_chain==True:
                if self.in_chain==False or self.first_in_chain==True:
                    if self.felt_eddy>0 or bullet2.felt_eddy>0:
                        #print('hit')
                        self.rect.left = bul2_rec.right
                        self.rect.top = bul2_rec.centery
                        self.bullet_speedx = bullet2.bullet_speedx
                        self.bullet_speedy = bullet2.bullet_speedy
                        
                        self.felt_eddy += 1
                        bullet2.felt_eddy += 1
                        new_num = self.num_cells + bullet2.num_cells
                        self.num_cells = new_num
                        bullet2.num_cells = new_num
                            
                        
                        if bullet2.in_chain==False:
                            bullet2.first_in_chain = True
                        if self.in_chain==False:
                            self.last_in_chain = True
                        
                        self.first_in_chain = False
                        bullet2.last_in_chain = False
                        self.in_chain = True
                        bullet2.in_chain = True
                        stats.score+= new_num
                        if stats.score>stats.high_score:
                            stats.high_score = stats.score
            else:
                if (self.bullet_speedx>0 and bullet2.bullet_speedx>0) or (self.bullet_speedx<0 and bullet2.bullet_speedx<0):
                    #print('yes')
                    xory = random.randrange(-1,2,2)
                    if xory==-1:
                        self.bullet_speedx *= -1
                    else:
                        bullet2.bullet_speedx *= -1
                        #self.bullet_speedy *= -1
                if (self.bullet_speedy>0 and bullet2.bullet_speedy>0) or (self.bullet_speedy<0 and bullet2.bullet_speedy<0):
                    #print('yes')
                    xory = random.randrange(-1,2,2)
                    if xory==-1:
                        self.bullet_speedy *= -1
                    else:
                        bullet2.bullet_speedy *= -1
                        #self.bullet_speedy *= -1
        
        
            
        
        
    
    
