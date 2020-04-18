from engine.metaGame import MetaGame
from .level import ExampleLevel
from .unit import Unit
from .plant import Plant

from .ui.screens import testGui, noGui, taskManagerGui
from engine.constants import SWIDTH, SHEIGTH
from .task import Task
from .task_steps import FARM, GO_HOME


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

        self.entities.append(Unit(self, (500.0, 500.0)))
        self.entities.append(Unit(self, (0.0, 200.0)))
        self.entities.append(Plant(self, (0.0, 0.0), 0))

        self.level = ExampleLevel(self)

        self.tasks = [Task("Testitaski", [FARM]), Task("Toinen Testitaski", [GO_HOME])]
        self.load_gui(taskManagerGui(self, self.tasks))

    def TEST_TASK_MANAGER(self):
        self.tasks = [Task("Testitaski", [FARM]), Task("Toinen Testitaski", [GO_HOME])]
        self.load_gui(taskManagerGui(self, self.tasks))
