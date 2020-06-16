from ressources.scenes.menu import menu
from ressources.scenes.game import game
from ressources.scenes.option import option
from ressources.scenes.shop import shop

from ressources.functions import *
from ressources.classes.player import Player
from ressources.ressources import *

# menu(game(Player(0, screen.get_height()-screen.get_height()/4)))
game(load(Player(0, screen.get_height()-screen.get_height()/4)))
# shop()

#menu()
game()
#shop()