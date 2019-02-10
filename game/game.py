from engine.metaGame import MetaGame
from .level import ExampleLevel
from .unit import Unit

from .ui.screens import testGui, noGui
from engine.constants import SWIDTH, SHEIGTH


class Game(MetaGame):
  def __init__(self, ENGINE):
    super().__init__(ENGINE)

    self.add_guiport("GUI", SWIDTH, SHEIGTH)

    # TODO make testgui less test. A single object with members as presets
    self.load_gui(testGui(self))

  def tick(self):
    super().tick()

  def START(self):
    self.add_cameraport("GAME", SWIDTH, SHEIGTH)

    # self.entities.append(Unit(self, (500.0, 500.0), (-.1, -.1)))
    self.entities.append(Unit(self, (0.0, 200.0), (.1, .1)))
    self.level = ExampleLevel(self)

    self.load_gui(noGui(self))
