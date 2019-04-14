
#GAME FUNCTION FILE SETUP


#regular code directory setup:
import sys, os, os.path
cwd = os.getcwd()
main_dirc = cwd.split('bell_algae_game', 1)[0]
cwd_code = main_dirc + 'bell_algae_game/code'
sys.path.insert(0, cwd_code+'/game_objects')

from alga import Alga
from swirl import Swirl1
#from alga_group import Clump

#general modules 
from time import sleep #pauses game when loss a life/ship
import pygame
import random 
import numpy as np

img_path = main_dirc+'/bell_algae_game/images/'
