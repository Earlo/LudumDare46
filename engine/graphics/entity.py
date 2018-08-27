import pygame

from .sprite import Sprite


class Entity(Sprite):
  def __init__(self, GAME, pos, time=pygame.time.get_ticks()):
    super().__init__(GAME, "sprites")
    self.topleft = pos
    self.created_at = time
    self.updated_at = self.created_at
    self.timeInterval = 0

  @property
  def age(self):
    return self.updated_at - self.created_at

  def update(self, t):
    self.timeInterval = t - self.lastUpdated
    self.lastUpdated = t

  def update_real_time(self):
    self.update(pygame.time.get_ticks())

  # TODO add dunders
