# NOTE just an example
# Only god can judge me


class Level:

  def __init__(self, GAME):
    self.GAME = GAME
    self.GAME.ENGINE.background_tile = self.background_tile

  def tick(self):
    pass


class ExampleLevel(Level):
  background_tile = "checker_dark"

  def __init__(self, GAME):
    super().__init__(GAME)

  def tick(self):
    super().tick()
