from ..task import Task
from ..unit_logic import task_steps


class MoveTo(Task):
    def __init__(self, target, assignee=None):
        title = "Moving to " + str(target)
        steps = [task_steps.MoveTo(target)]
        super().__init__(title, steps, assignee)


class PlantOlives(Task):
    def __init__(self, target, assignee=None):
        title = "Plant olives at " + str(target)
        steps = [task_steps.MoveTo(target), task_steps.PlantStep(target)]
        super().__init__(title, steps, assignee)
