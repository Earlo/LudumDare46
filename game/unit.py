
from engine.graphics.entity import Entity


# Example of a thing that does something
class Unit(Entity):
  sprite = ['frog']
  graphic_layer = 1

  def __init__(self, GAME):
    super().__init__(GAME, (0.0, 0.0))

  def tick(self):
    self.move_ip(1, 1)
    self.draw()
