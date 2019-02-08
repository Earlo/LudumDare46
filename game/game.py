from engine.metaGame import MetaGame
from .level import ExampleLevel
from .unit import Unit

from .ui.screens import testGui


class Game(MetaGame):
  def __init__(self, ENGINE):
    super().__init__(ENGINE)
    self.entities.append(Unit(self))
    self.level = ExampleLevel(self)

    # TODO make testgui less test. A single object with members as presets
    self.load_gui(testGui())

  def tick(self):
    super().tick()

  def STARTGAME(self):
    self.on_tick_action = self.game_tick

