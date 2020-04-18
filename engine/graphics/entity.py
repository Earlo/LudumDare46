import pygame

from .sprite import Sprite
from ..window.viewportHandler import ViewportHandler


class Entity(Sprite):
    def __init__(self, pos, time=pygame.time.get_ticks()):
        super().__init__(ViewportHandler().viewPorts["GAME"], "sprites")
        self.float_pos = pos
        self.topleft = pos
        self.created_at = time
        self.updated_at = self.created_at
        self.timeInterval = 0

    def tick(self, t):
        self.timeInterval = t
        movement = [x * self.timeInterval for x in self.velocity]
        self.float_pos = tuple(map(sum, zip(self.float_pos, movement)))
        self.topleft = self.float_pos
        self.updated_at = pygame.time.get_ticks()
        self.draw()

    def _real_time_tick(self):
        Entity.tick(self, pygame.time.get_ticks())

    @property
    def age(self):
        return self.updated_at() - self.created_at
