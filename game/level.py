import pygame
import itertools


# TODO refactor
class Level(pygame.Rect):
  sprites = []
  bgr_depth = 0

  def __init__(self, GAME):
    self.GAME = GAME
    # TODO is tile, not sprite
    self._sprite = self.sprites[0]
    super().__init__((0, 0), (760, 500))

  # TODO make the getter setter thing
  def sprite(self):
     # TODO Pass only strings to Engine
     return self.GAME.ENGINE.graphical_asset_handler["bgr"][self._sprite]

  # TODO move
  # TODO this method blits, doesn't draw
  def draw(self):
    tile_w, tile_h = self.sprite().get_width(), self.sprite().get_height()

    for x, y in itertools.product(range(0, self.w + 1, tile_w),
                                  range(0, self.h + 1, tile_h)):
      self.GAME.ENGINE.surf_BGR.blit(self.sprite(), (x, y), self)

    self.GAME.ENGINE.updates[self.bgr_depth].append((self.GAME.ENGINE.surf_BGR, self))

  def tick(self):
    # TODO Move to draw in engine side
    # TODO Only call when needed
    self.draw()


class ExampleLevel(Level):
  sprites = ["checker_dark"]

  def __init__(self, GAME):
    super().__init__(GAME)
    self._sprite = self.sprites[0]

  def tick(self):
    super().tick()
