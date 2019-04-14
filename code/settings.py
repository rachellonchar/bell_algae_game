
class Settings():
    '''A class to store all settings for game alien invasion'''
    def __init__(self):
        '''Initialize game (static) settings'''
        #screen settings
        self.screen_width = 1366#1000
        self.screen_height = 768#700
        self.bg_color = (194,194,251)
        
        #game speed
        self.speedup_scale = 1 #1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
        #eddy settings
        self.ed_px_width = 3
        self.ed_px_height = 3
        self.eddy_color = (100,100,250)
    
    def initialize_dynamic_settings(self):
        '''settings that change with the game'''

        self.bullet_speed_factor = 1
        
        #eddy settings
        self.ed_speed_factor = 1
        self.ed_size = 220
        
        #scoring
        #self.alien_points = 50
        
    def increase_speed(self):
        '''increase speed settings'''
        
        #self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        #self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points*self.score_scale)
    def update_eddy_size(self,increm):
        self.ed_size += increm
    

        
    
    
