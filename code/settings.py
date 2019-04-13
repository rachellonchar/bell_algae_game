
class Settings():
    '''A class to store all settings for game alien invasion'''
    def __init__(self):
        '''Initialize game (static) settings'''
        #screen settings
        self.screen_width = 1000#1366
        self.screen_height = 700#768
        self.bg_color = (194,194,251)
        
        #ship settings 
        self.ship_limit = 2
        
        #bullet settings
        self.bullet_width = 9
        self.bullet_height = 9
        self.bullet_color = (0,87,0)
        self.bullets_allowed = 5
        
        #branch bit settings
        self.bb_width = 11
        self.bb_height = 200
        self.bb_color = (100,100,0)
        self.bb_prev_locx = 3/4*(self.screen_width)
        self.bb_prev_locy = 0
        
        #alien settings
        self.fleet_drop_speed = 10
        
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
        #self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 0.5
        
        #eddy settings
        self.ed_speed_factor = 1
        self.ed_size = 200
        #self.eddy_reductions = 5
        #self.eddy_reduction_factor = 2/3
        #self.straight_away_factor = 1/3
        
        #scoring
        self.alien_points = 50
        
    def increase_speed(self):
        '''increase speed settings'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
    def update_eddy_size(self,increm):
        self.ed_size += increm
    
    #def update_swirl_loc(self,mouse_x,mouse_y):
        #self.swirl_start_x = mouse_x
        #self.swirl_start_y = mouse_y
        ##self.swirl_size = swirl_sz
        
    
    
