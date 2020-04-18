from task import Task
from unit_logic import task_steps


class MoveTo(Task):
    def __init__(self, target):
        title = "Moving to " + str(target)
        steps = [task_steps.MoveTo(target)]
        super().__init__(title, steps)
