from engine.metaGame import MetaGame
from .level import ExampleLevel
from .unit import Unit

from .ui.screens import testGui


class Game(MetaGame):
  def __init__(self, ENGINE):
    super().__init__(ENGINE)

    # TODO make testgui less test. A single object with members as presets
    self.load_gui(testGui(self))

  def tick(self):
    super().tick()

  def START(self):
    print(self.entities)
    self.entities.append(Unit(self))
    self.level = ExampleLevel(self)
