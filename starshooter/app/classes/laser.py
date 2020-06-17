from app.ressources import *

from app.classes.projectile import Projectile


class Laser(Projectile):
    def __init__(self, x, y, is_player, param):
        super().__init__(x, y, is_player, 'laser', param)

    def move(self):
        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed
        
    def draw(self):
        pg.draw.rect(screen, self.color, ((int(self.x - self.surface.get_width()/2), int(self.y)), self.surface.get_size()))