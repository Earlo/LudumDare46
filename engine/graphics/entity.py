import pygame

from .sprite import Sprite

class Entity(Sprite):
  def __init__(self, GAME, pos, time=pygame.time.get_ticks()):
    super().__init__(GAME, "sprites")
    self.topleft = pos
    self.float_pos = pos
    self.created_at = time
    # self.updated_at = self.created_at
    self.timeInterval = 0

    self.velocity = (0.001, 0.001)

  def tick(self, t):
    self.timeInterval = t

    movement = [x * self.timeInterval for x in self.velocity]
    self.float_pos = tuple(map(sum, zip(self.float_pos, movement)))
    self.topleft = self.float_pos

    self.draw()

  def _real_time_tick(self):
    Entity.tick(self, pygame.time.get_ticks())

  # TODO add dunders

  @property
  def age(self):
    return self.updated_at - self.created_at
