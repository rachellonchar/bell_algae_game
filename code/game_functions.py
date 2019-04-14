
##ALIEN INVASION 
#  IN-GAME FUNCTIONS/MOVEMENTS 

#regular code directory setup:
import sys, os, os.path
cwd = os.getcwd()
main_dirc = cwd.split('bell_algae_game', 1)[0]
cwd_code = main_dirc + 'bell_algae_game/code'
sys.path.insert(0, cwd_code+'/game_functions')

from key_funcs import *
