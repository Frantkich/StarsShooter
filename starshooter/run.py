from app.ressources import *


from app.scenes.inventory import inventory
from app.scenes.option import option
from app.scenes.menu import menu
from app.scenes.game import game
from app.scenes.shop import shop

from app.classes.player import Player

# menu()
#game(load(Player(screen.get_width()/2, screen.get_height()-screen.get_height()/4)))
#shop()
inventory(Player(screen.get_width()/2, screen.get_height()-screen.get_height()/4))
