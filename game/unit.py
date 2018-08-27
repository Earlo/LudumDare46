
from engine.graphics.entity import Entity


# Example of a thing that does something
class Unit(Entity):
  sprite = ['frog']
  graphic_layer = 1

  def __init__(self, GAME):
    super().__init__(GAME, (100.0, 100.0))

  def tick(self):
    # Should most likely use tick
    super().real_time_tick()
