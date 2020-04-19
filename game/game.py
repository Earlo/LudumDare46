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
        # Mouse was clicked
        if self.hasStarted and self._ENGINE.mouse[1]:
            self.taskManager.add_task(
                MoveTo(
                    [x + y for x, y in zip(self._ENGINE.mouse[0], self.camera_offset)]
                )
            )

        super().tick()

    def START(self):
        self.add_cameraport("GAME", SWIDTH, SHEIGTH)

        units = [Unit(self, (0.0, 200.0))]
        for unit in units:
            self.entities.append(unit)
            self.taskManager.add_to_pool(unit)
        self.entities.append(Plant(self, (0.0, 0.0), 0))
        self.entities.append(Home(self, (100.0, 100.0)))

        self.level = ExampleLevel(self)
        self.load_gui(taskManagerGui(self, self.taskManager.activeTasks))
        self.hasStarted = True

    def TEST_TASK_MANAGER(self):
        self.tasks = [Task("Testitaski", [FARM]), Task("Toinen Testitaski", [GO_HOME])]
        self.load_gui(taskManagerGui(self, self.tasks))
