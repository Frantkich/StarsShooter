from app.ressources import *


class Explosion:
  def __init__(self, pos, size):
    self.x, self.y = pos 
    self.size = size
    self.particles = []
    self.particle(self.size)

  def particle(self, size):
    explosion = [(193, 48, 28), (251, 222, 159), (242, 156, 22)]
    # explosion = [(238, 240, 240), (42, 201, 250), (143, 228, 246), (142, 67, 216)]
    for loop in range(random.randint(int(size*0.5), int(size*1.5))):
      self.particles.append([[self.x, self.y], [random.uniform(-1, 1), random.uniform(-1, 1)], random.randint(int(size*0.05), int(size*0.15)), random.uniform(int(size*0.01), int(size*0.10)), random.choice(explosion)])

  def draw(self):
    for particle in self.particles:
      particle[0][0] += particle[1][0]*particle[3]
      particle[0][1] += particle[1][1]*particle[3]
      particle[2] -= 0.5
      pg.draw.circle(screen, particle[4], [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
      if particle[2] <= 0:
          self.particles.remove(particle)
