
##ALIEN INVASION 
#  FONT
#scoreboard
import pygame.font



class Scoreboard():
    '''class to report scoring info'''
    def __init__(self,ai_settings,screen,stats):
        '''initialize scoreboard'''
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        #font settings
        self.text_color = (30,100,40)
        self.level_color = (200,10,10)
        self.font = pygame.font.SysFont(None,40)
        
        #prep initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
    
    def prep_score(self):
        '''turn the score into a rendered image'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = '{:,}'.format(rounded_score)
        #self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        self.score_image = self.font.render('',True,self.text_color,self.ai_settings.bg_color)
        
        #display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        #draw score
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
    
    def prep_high_score(self):
        '''turn high score into rendered image'''
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render('microcystis aeruginosa',True,self.text_color,self.ai_settings.bg_color)
        #self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        
        #center high score at top of screen
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        #self.level_image = self.font.render('microcystis aeruginosa',True,self.text_color,self.ai_settings.bg_color)
        self.level_image = self.font.render('',True,self.text_color,self.ai_settings.bg_color)
        
        #position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = self.score_rect.top
        
        
        
