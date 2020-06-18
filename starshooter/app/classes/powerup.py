from app.ressources import *


class PowerUp:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.img, self.time, self.mod, self.price = powerup_list[name]
        self.path, self.nbframe = self.img
        self.img = pg.image.load(self.path)
        self.init_sprites(self.img)

        self.speed = 5
        self.time *= fps
        self.save = ()

    def init_sprites(self, img):
        self.sprites = spritesheet(img, self.nbframe)
        self.sprite = self.sprites[0]
        self.mask = pg.mask.from_surface(self.sprite)
        self.frame = 0
        self.nextFrame = 0

    def update_sprite(self):
        if self.nextFrame == 0:
            self.frame = (self.frame + 1) % self.nbframe
            self.sprite = self.sprites[self.frame]
            self.mask = pg.mask.from_surface(self.sprite)
            self.nextFrame = gif_speed
            self.nextFrame -= 1
        self.nextFrame -= 1

    def move(self, objs):
        if objs:
            if objs[0].is_player:
                self.y += self.speed
            else:
                self.y -= self.speed
        else:
            self.y -= self.speed

    def check_time(self, obj):
        if 0 < self.time:
            self.time -= 1
        else:
            self.effect(obj, 0)
            obj.powerups.remove(self)
            
    def effect(self, obj, add):
        if self.name == "speed" or self.name == "slow":
            if add:
                self.save = (obj.speed)
                obj.speed *= self.mod
            else:
                obj.speed = self.save
        if self.name == "heal":
            obj.health = obj.health_max
        if self.name == "money":
            obj.money += 2500
        if self.name == "damage" or self.name == "weak":
            if add:
                obj.damage_mod = self.mod
            else:
                obj.damage_mod = 1
        if self.name == "firerate":
            if add:
                obj.firerateMod = self.mod
            else:
                obj.firerateMod = 1

        if self.name == "size" or self.name == "bigboi":
            if add:
                self.save = (obj.img)
                obj.init_sprites(pg.transform.scale(obj.img, (int(obj.img.get_width() * self.mod), int(obj.img.get_height() * self.mod))))
                obj.size_mod = self.mod 
            else:
                obj.img = self.save
                obj.init_sprites(obj.img)
                obj.size_mod = 1
        if self.name == "cooldown":
            if obj.is_player:
                if add:
                    if obj.weapons[obj.slot_active].weapon:
                        self.save = (obj.weapons[obj.slot_active].cooldown_max, obj.slot_active)
                        obj.weapons[obj.slot_active].cooldown_max = int(obj.weapons[obj.slot_active].cooldown_max * self.mod)
                        obj.weapons[obj.slot_active].cooldown = int(obj.weapons[obj.slot_active].cooldown_max * self.mod)
                else:
                    if self.save:
                        obj.weapons[self.save[1]].cooldown_max = self.save[0]
                        obj.weapons[self.save[1]].cooldown *= 0
            else:
                if add:
                    obj.firerateMod = self.mod
                else:
                    obj.firerateMod = 1

    def update(self, objs):
        self.update_sprite()
        self.move(objs)
        if screen.get_height() < self.y:
            return self
        for obj in objs:
            if collide(self, obj):
                for powerup in obj.powerups:
                    if powerup.name == self.name:
                        powerup.time += self.time
                        return self
                obj.powerups.append(self)
                self.effect(obj, 1)
                return self

    def draw(self):
        screen.blit(self.sprite, (self.x, int(self.y)))
