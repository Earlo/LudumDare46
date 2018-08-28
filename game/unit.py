from engine.graphics.entity import Entity


class Unit(Entity):
  sprite = ['frog']
  graphic_layer = 1

  def __init__(self, GAME):
    super().__init__(GAME, (0.0, 200.0))

  def tick(self, t):
    super().tick(t)
