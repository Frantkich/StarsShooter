import pygame as pg
import random
class Star:
    def __init__(self, pos, width, heritage=None):
        self.x, self.y = pos
        if heritage:
            self.width = width
        else:
            if 0 <= width < 80:
                self.width = 0
            if 80 <= width < 95:
                self.width = 1
            if 95 <= width <= 100:
                self.width = 2
        self.color = (255, 240, 200)
        self.vel = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.acc = (random.uniform(0.005, 0.05) * self.width) + 1
        if not(self.acc):
            self.acc = 1.005

    def move(self):
        self.vel[0] *= self.acc
        self.vel[1] *= self.acc
        
        self.x += self.vel[0]
        self.y += self.vel[1]
    
    def draw(self, surface):
        if 0 < self.x < surface.get_width() or 0 < self.y < surface.get_height():
            pg.draw.line(surface, (255, 240, 200), (int(self.x - self.vel[0]), int(self.y - self.vel[1])), (int(self.x), int(self.y)), self.width)
            if self.width:
                pg.draw.circle(surface, (255, 240, 200), (int(self.x), int(self.y)), self.width)
            else:
                surface.set_at((int(self.x), int(self.y)), self.color)
        else:
            return True
     