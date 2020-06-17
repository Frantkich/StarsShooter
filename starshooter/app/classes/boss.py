from app.ressources import *

from app.classes.ship import Ship


class Boss(Ship):
    def __init__(self, x, y, model):
        super().__init__(x, y, model)
        self.firerateMod = 1
        self.destX = int(screen.get_width()/2 - self.get_width()/2)
        self.destY = int(random.randint(0, int(screen.get_height()/2)))

        # self.destX = self.x+0.1
        # self.destY = self.y+0.1

    # def newDest(self, dist, distX, distY):
    #     self.destX = random.randint(0, screen.get_width() - self.get_width())
    #     self.destY = random.randint(0, int(screen.get_height()/4))

    #     self.dirX = distX / dist
    #     self.dirY = distY / dist

    def move(self):
        self.distX = self.destX - self.x
        self.distY = self.destY - self.y
        dist = math.hypot(self.distX, self.distY)
        self.dirX = self.distX / dist
        self.dirY = self.distY / dist

        self.x += self.dirX * self.speed
        self.y += self.dirY * self.speed

        if dist < self.speed: 
            self.destX = random.randint(0, screen.get_width() - self.get_width())
            self.destY = random.randint(0, int(screen.get_height()/4))
        
        # self.distX = self.destX - self.x
        # self.distY = self.destY - self.y
        # dist = math.hypot(self.distX, self.distY)
        
        # if math.hypot(self.destX - self.x, self.destY - self.y) < self.speed: 
        #     self.newDest(math.hypot(self.destX - self.x, self.destY - self.y), self.destX - self.x, self.destY - self.y)
        # else:
        #     self.x += self.dirX * self.speed
        #     self.y += self.dirY * self.speed


    def update(self, targets):
        target = targets[0]
        if self.health <= 0:
            return self
        if random.randrange(0, fps * self.firerateMod) == 1:
            for self.slot_active in range(len(self.weapons)):
                self.shoot()
        if collide(self, target):
            target.money += 1000
            target.score += 1000
            return self
        self.move()
        self.update_all(targets)