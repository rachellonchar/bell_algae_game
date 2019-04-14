


# INSTRUCTIONS

# click f5 to start the program
# click play to start
# click mouse to create eddy/whirlpool at that location
# to increase or decrease eddy size, use the up and down keys
# to restart to game press the space bar



# PURPOSE

# this species of algae has survived several mass extinction events
# new research done by Jackie Taylor of Saint Anthony Falls Lab in Minneapolis found that algae cells group together under stress
# this mutual aid strategy is likely why they have survived through so many mass extincition events
# turbulence is stressful for algae (this is why you only see that green scummy stuff---which is algae---in standing water like ponds)
# when the water is moving too rapidly, algae can't survive (e.g. rivers)
# as you increase the size of the eddies, the algae will have a hard time surviving,
# but they will group together and this strategy allows them to percervere through harsh conditions
# this type of algae also group up when zooplankton are present b/c zooplankton eat them


# IGNORE BEYOND THIS LINE -----------------------------------------------------------------------------
import sys, os, os.path
cwd = os.getcwd()
main_dirc = cwd.split('bell_algae_game', 1)[0]
cwd_code = main_dirc + 'bell_algae_game/code'
sys.path.insert(0, cwd_code)
from algae_fun import *
#--------------------------------------------------------------------------------------------
