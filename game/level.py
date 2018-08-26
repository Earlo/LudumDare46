import pygame
import itertools

from engine.graphics.entity import Sprite


# TODO refactor
class Level(Sprite):
  bgr_depth = 0

  def __init__(self, GAME):
    self.GAME = GAME
    super().__init__(GAME, "bgr")

  def tick(self):
    # TODO Move to draw in engine side
    # TODO Only call when needed
    self.draw()


class ExampleLevel(Level):
  sprites = ["checker_dark"]

  def __init__(self, GAME):
    super().__init__(GAME)

    # Example of repeating background
    bgr = pygame.Surface([self.w * 3, self.h * 3], pygame.HWSURFACE)
    for x, y in itertools.product(range(0, 400, self.w),
                                  range(0, 500, self.h)):
      GAME.ENGINE.surf_BGR.blit(self.surf, (x, y), self)
    self.surf = GAME.ENGINE.surf_BGR

  def tick(self):
    super().tick()
