class ExampleLevel:
  background = "checker_dark"

  def __init__(self, GAME):
    self.GAME = GAME
    self.GAME.ENGINE.background_tile = self.background
