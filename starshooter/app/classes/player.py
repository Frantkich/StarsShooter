from app.ressources import *

from app.classes.ship import Ship
from app.classes.label import Label
from app.classes.powerup import PowerUp


class Player(Ship):
    def __init__(self, x, y):
        super().__init__(x, y, 'player', 1)
        self.screen_shake = 0
        self.money = 500
        self.score = 0
        self.max_score = 0
        #items
        self.items = []
        self.item_cooldown = 30
        self.inventory = {
            'ships': ['player'],
            'weapons': [],
            'slow': 0,
            'weak': 0,
            'bigboi': 0,
            'firerate': 0
        }
        #Rect((screen, (255, 0, 0), (screen.get_width() - offset - width, screen.get_height() - int(height/2) - thickness - offset, width, int(height/2)))
        self.healthbar_component = [
            pg.Rect((screen.get_width() - 160, screen.get_height() - 40, 150, 25)),
            pg.Rect((screen.get_width() - 160, screen.get_height() - 40, 150*(self.health/self.health_max), 25)),
            Label(screen.get_width() - 87, screen.get_height() - 50, self.name, (255, 240, 200), 20),
            pg.Rect((screen.get_width() - 160, screen.get_height() - 65, 150, 50))
        ]
        self.inventory_componenet = [
            
        ]
    def move(self):
        if keyPressed("q") and self.x - self.speed > 0:
            self.x -= self.speed
        if keyPressed("d") and self.x + self.speed + self.get_width() < screen.get_width():
            self.x += self.speed
        if keyPressed("z") and self.y - self.speed > 0:
            self.y -= self.speed
        if keyPressed("s") and self.y + self.speed + self.get_height() + self.speed < screen.get_height():
            self.y += self.speed

    def check_shoot(self):
        if keyPressed("space"):
            self.shoot()

    def use_item(self, targets):
        if not(self.item_cooldown):
            if keyPressed("w") and 0 < self.inventory['slow']:
                self.items.append(PowerUp(self.x, self.y, "slow"))
                self.inventory['slow'] -=1
                self.item_cooldown = 30
            if keyPressed("x") and 0 < self.inventory['weak']:
                self.items.append(PowerUp(self.x, self.y, "weak"))
                self.inventory['weak'] -=1
                self.item_cooldown = 30
            if keyPressed("c") and 0 < self.inventory['bigboi']:
                self.items.append(PowerUp(self.x, self.y, "bigboi"))
                self.inventory['bigboi'] -=1
                self.item_cooldown = 30
            if keyPressed("v") and 0 < self.inventory['firerate']:
                self.items.append(PowerUp(self.x, self.y, "firerate"))
                self.inventory['firerate'] -=1
                self.item_cooldown = 30
        elif 0 < self.item_cooldown:
            self.item_cooldown -= 1

    def update_items(self, targets):
        for item in self.items[:]:
            item_temp = item.update(targets)
            if item_temp:
                self.items.remove(item_temp)

    def update(self, targets):
        if self.health <= 0:
            self.health = 0
            if self.max_score < self.score:
                self.max_score = self.score
            self.score = 0
            return True
        self.move()
        self.check_shoot()
        self.use_item(targets)
        self.update_items(targets)
        self.update_all(targets)

    def weapon_switch(self, key):
        if 0 <= key < len(self.weapons):
            self.slot_active = key

    def loose_health(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        self.healthbar_component[1] = (screen.get_width() - 160, screen.get_height() - 40, 150*(self.health/self.health_max), 25)

    def healthbar(self):
        pg.draw.rect(screen, (255, 0, 0), self.healthbar_component[0])
        pg.draw.rect(screen, (0, 255, 0), self.healthbar_component[1])
        self.healthbar_component[2].draw()
        pg.draw.rect(screen, (255, 240, 200), self.healthbar_component[3], 5)
        pg.draw.line(screen, (255, 240, 200), (screen.get_width() - 160, screen.get_height() - 40), (screen.get_width() - 10, screen.get_height() - 40), 5)

    def inventory_hud(self):
        color = (255, 240, 200)
        for item in self.items:
            item.draw()
        height = 125
        for powerup in self.powerups:
            Label(12, screen.get_height() - height, ' :'.join((powerup.name, str(int(powerup.time / fps)))), color, 20).draw(0, 1)
            height += 25
        height = 125
        for item in list(self.inventory.keys())[2:]:
            Label(screen.get_width() - 25, screen.get_height() - height, ' :'.join((item, str(self.inventory[item]))), color, 20).draw(0, 2)
            height += 25

    def draw(self):
        super().draw()
        self.healthbar()
        self.weapons[self.slot_active].draw() 
        self.inventory_hud()