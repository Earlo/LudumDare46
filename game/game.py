from engine.metaGame import MetaGame
from .level import ExampleLevel
from .units.unit import Unit
from .units.plant import Plant
from .buildings.home import Home

from .ui.screens import testGui, noGui, taskManagerGui
from engine.constants import SWIDTH, SHEIGTH
from .task_manager import TaskManager
from .task import Task
from .unit_logic.task_steps import FARM, GO_HOME
from .unit_logic.tasks import MoveTo


class Game(MetaGame):
    def __init__(self, ENGINE):
        super().__init__(ENGINE)
        # resource array
        self.resources = {"olives": 0}
        self.add_guiport("GUI", SWIDTH, SHEIGTH)
        self.taskManager = TaskManager(self)

        # TODO make testgui less test. A single object with members as presets

        self.load_gui(testGui(self))

    def tick(self):
        super().tick()

    def START(self):
        self.add_cameraport("GAME", SWIDTH, SHEIGTH)

        units = [Unit(self, (500.0, 500.0)), Unit(self, (0.0, 200.0))]
        tasks = [
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
            MoveTo([100, 100]),
        ]
        for unit in units:
            self.entities.append(unit)
        for task in tasks:
            self.taskManager.assign_task(task)
        self.entities.append(Plant(self, (0.0, 0.0), 0))
        self.entities.append(Home(self, (100.0, 100.0)))
        self.taskManager.add_to_pool(*units)

        self.level = ExampleLevel(self)

        self.load_gui(taskManagerGui(self, self.taskManager.active_tasks))

    def TEST_TASK_MANAGER(self):
        self.tasks = [Task("Testitaski", [FARM]), Task("Toinen Testitaski", [GO_HOME])]
        self.load_gui(taskManagerGui(self, self.tasks))
