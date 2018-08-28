from engine.metaGame import MetaGame
from .level import ExampleLevel
from .unit import Unit


class Game(MetaGame):
  def __init__(self, ENGINE):
    super().__init__(ENGINE)
    self.entities = [Unit(self)]
    self.level = ExampleLevel(self)

  def tick(self):
    time = self.ENGINE.clock.get_ticks()
    for e in self.entities:
      e.tick(time)
