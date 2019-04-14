
##ALIEN INVASION 
#  FONT
#start button
import pygame.font



class Button():
    def __init__(self,ai_settings,screen,msg):
        '''initialize button attributes'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (20,200,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #build button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #the button message only needs to be prepped once
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        '''turn msg into a rendered image and center text on the button'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #true sets text background color to specified background color
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #draw blank button
        self.screen.fill(self.button_color, self.rect)
            
        #draw text onto button
        self.screen.blit(self.msg_image, self.msg_image_rect)
    
