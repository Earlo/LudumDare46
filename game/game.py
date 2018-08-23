from engine.metaGame import MetaGame
from .level import ExampleLevel


# should it inherit engine? Maybe?
class Game(MetaGame):
  def __init__(self, ENGINE):
    super().__init__(ENGINE)

    self.pos = [0, 0]
    self.entities = []
    self.level = ExampleLevel(self)

  def tick(self):
    self.level.tick()
    for e in self.entities:
      e.tick()
