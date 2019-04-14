
##ALIEN INVASION 
#  track game stats



class GameStats():
    '''track game stats for alien invasion'''
    
    def __init__(self,ai_settings):
        '''initialize stat report'''
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #high score shouldn't be reset
        self.high_score = 0
        
        #start game in an inactive status
        self.game_active = False
    
    def reset_stats(self):
        #self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
