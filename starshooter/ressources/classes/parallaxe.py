import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *


class Parallaxe:
  def __init__(self, param):
    self.path, self.nbframe, self.speed = parallaxe_list[param]
    self.img = pygame.image.load(self.path)
    self.dist = random.uniform(0.25, 0.75)
    self.img = pg.transform.scale(self.img, (int(self.img.get_width()*self.dist), int(self.img.get_height()*self.dist)))

    self.width, self.height = self.img.get_size()

    self.img = pg.transform.smoothscale(self.img, (int(self.width*self.dist*0.75), int(self.height*self.dist*0.75)))
    self.img = pg.transform.smoothscale(self.img, (self.width, self.height))

    self.init_sprites(self.img)

    self.x = random.randint(0 - self.sprites[0].get_width(), screen.get_width())
    self.y = -self.sprites[0].get_height()
    # self.y = random.randint(-screen.get_height(),-self.sprites[0].get_height())
    self.speed *= self.dist 

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

  def update_all(self, targets):
    self.update_sprite()
    self.move()

  def move(self):
      self.y += self.speed

  def draw(self):
    screen.blit(self.sprite, (self.x, int(self.y)))

  def off_screen(self, width, height):
    return self.x + self.surface.get_width() < 0 or width < self.x or self.y + self.surface.get_height() < 0 or height < self.y
