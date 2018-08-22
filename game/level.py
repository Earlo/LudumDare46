import pygame


# TODO refactor
class Level(pygame.Rect):
  sprites = []

  def __init__(self, GAME):
    self.GAME = GAME
    self._sprite = self.sprites[0]
    super().__init__((0, 0), (200, 200))

  # TODO make the getter setter thing
  def sprite(self):
     # TODO Pass only strings to Engine
     return self.GAME.ENGINE.graphical_asset_handler["BGR"][self._sprite]

  def tick(self):
    # TODO Move to draw in engine side
    self.GAME.ENGINE.surf_BGR.blit(self.sprite(), (0, 0), self)


class ExampleLevel(Level):
  sprites = ["checker_dark"]

  def __init__(self, GAME):
    super().__init__(GAME)
    self._sprite = self.sprites[0]

  def tick(self):
    super().tick()
