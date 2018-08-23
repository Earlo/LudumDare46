import pygame
import itertools

from engine.graphics.entity import Sprite


# TODO refactor
class Level(Sprite):
  bgr_depth = 0

  def __init__(self, GAME):
    self.GAME = GAME
    super().__init__(GAME, "bgr")

  # TODO move
  # TODO this method blits, doesn't draw
  def draw(self):
    self.GAME.ENGINE.updates[self.bgr_depth].append((self.surf, self))

  def tick(self):
    # TODO Move to draw in engine side
    # TODO Only call when needed
    self.draw()


class ExampleLevel(Level):
  sprites = ["checker_dark"]

  def __init__(self, GAME):
    super().__init__(GAME)
    # Example of repeating background
    bgr = pygame.Surface([self.w * 3, self.h * 3])
    for x, y in itertools.product(range(0, bgr.get_width(), self.w),
                                  range(0, bgr.get_height(), self.h)):
      bgr.blit(self.surf, (x, y), self)
    self.surf = bgr

  def tick(self):
    super().tick()
