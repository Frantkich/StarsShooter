class PowerUp:
  def __init__():
    def __init__(self, x, y, param):
        self.x = x
        self.y = y
        self.color, self.size, self.speed = param
        self.surface = pg.Surface(self.size)
        self.mask = pg.mask.from_surface(self.surface)

    def move(self):
          self.y += self.speed

    def draw(self, window):
        # pg.draw.rect(window, self.color, ((self.x - self.surface.get_width()/2, self.y), self.surface.get_size()))
        pg.draw.circle(window, self.color, (self.x, self.y), int(self.surface.get_height()/4), int(self.surface.get_width()/4), 1, 1)
        # pg.draw.ellipse(window, self.color, ((self.x - self.surface.get_width()/2, self.y), self.surface.get_size()))

    def off_screen(self, height):
        return self.y > height

    def collision(self, obj):
        return functions.collide(self, obj)

