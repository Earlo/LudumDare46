import pygame

from .sprite import Sprite


class Entity(Sprite):
  def __init__(self, GAME, pos, time):
    self.change_sprite_to(0)
    super().__init__(GAME, "sprites")

    self.GAME = GAME

    self.created_at = time
    self.updated_at = self.created_at
    self.timeInterval = 0
    self.center = pos
    self.float_pos = pos

  @property
  def age(self):
    return self.updated_at - self.created_at

  def update(self, t):
    self.timeInterval = t - self.lastUpdated
    self.lastUpdated = t

  def update_real_time(self):
    self.update(pygame.time.get_ticks())

  # TODO add dunders
