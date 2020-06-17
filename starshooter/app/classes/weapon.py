from app.ressources import *

from app.classes.laser import Laser
from app.classes.missile import Missile
from app.classes.label import Label


class Weapon:
    def __init__(self, pos, is_player, weapon=None):
        self.x, self.y = pos
        self.change_weapon(weapon)
        self.is_player = is_player

    def change_weapon(self, weapon):
        self.weapon = weapon
        if self.weapon:
            self.cooldown_max = weapon_list[self.weapon][0] * fps
            self.cooldown = 0

    def check_cooldown(self):
        if self.weapon:
            if self.cooldown < self.cooldown_max:
                self.cooldown += 1

    def shoot(self, shipX, shipY, sizeMod):
        if self.weapon:
            if self.cooldown == self.cooldown_max:
                self.cooldown = 0
                x = int(self.x * sizeMod)
                y = int(self.y * sizeMod)
                if self.weapon == 'missile':
                    return [Missile(shipX + x, shipY + y, self.is_player, weapon_list[self.weapon][1]) for _ in range(weapon_list[self.weapon][2])]
                else:
                    return [Laser(shipX + x, shipY + y - weapon_list[self.weapon][1][1][1] + weapon_list[self.weapon][1][3], self.is_player, weapon_list[self.weapon][1]) for _ in range(weapon_list[self.weapon][2])]
                            
    def cooldownbar(self):
        height = 50
        width = 150
        thickness = 5
        offset = 10
        color = (255, 240, 200)
        
        if self.weapon:
            if self.cooldown_max:
                if self.cooldown_max == -1:
                    ratio = 0
                else:
                    ratio = self.cooldown/self.cooldown_max
            else:
                ratio = 1
            pg.draw.rect(screen, (255, 0, 0), (offset, screen.get_height() - int(height/2) - thickness - offset, width, int(height/2)))
            pg.draw.rect(screen, (0, 255, 0), (offset, screen.get_height() - int(height/2) - thickness - offset, width*ratio, int(height/2)))
            Label((offset + width + thickness)/2, screen.get_height() - height, self.weapon, color, 20).draw()
        else:
            Label((offset + width + thickness)/2, screen.get_height() - height, "N/A", color, 20).draw()
        pg.draw.rect(screen, color, (offset, screen.get_height() - height - thickness - offset, width, height), thickness)
        pg.draw.line(screen, color, (offset, screen.get_height() - int(height/2) - thickness - offset), (offset + width, screen.get_height() - int(height/2) - thickness - offset), thickness)

    def draw(self):
        self.cooldownbar()
