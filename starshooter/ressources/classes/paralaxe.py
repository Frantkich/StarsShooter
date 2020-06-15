import pygame as pg
import random

from ressources.ressources import *
from ressources.settings import *
from ressources.functions import *


class Paralaxe:
  def __init__(self, param):
    self.speed, self.path, self.nbframe = spaceship_list[spaceship]
    self.img = pygame.image.load(self.path)
    self.init_sprites(self.img)
    self.x = random.randint(0 - self.sprites[0].get_width(), screen.get_width())
    self.y = random.randint(0 - self.sprites[0].get_height(), -screen.get_height()

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

  def draw(self, window):
    window.blit(self.sprite, (self.x, self.y))

  def off_screen(self, width, height):
    return self.x + self.surface.get_width() < 0 or width < self.x or self.y + self.surface.get_height() < 0 or height < self.y
