import pygame

from .sprite import Sprite


class Entity(Sprite):
  def __init__(self, GAME, pos, time=pygame.time.get_ticks()):
    super().__init__(GAME, "sprites")
    self.topleft = pos
    self.created_at = time
    self.updated_at = self.created_at
    self.timeInterval = 0

  def tick(self, t):
    self.timeInterval = t - self.updated_at
    self.updated_at = t
    # TODO remove
    self.move_ip(1, 1)

    self.draw()

  def _real_time_tick(self):
    Entity.tick(self, pygame.time.get_ticks())

  # TODO add dunders

  @property
  def age(self):
    return self.updated_at - self.created_at
