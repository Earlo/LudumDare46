from task_step import TaskStep

from math import atan2


class MoveTo(TaskStep):
    def __init__(self, target, *args, **kwargs):
        title = "Movine to " + str(target)
        super().__init__(title)
        self.target = target

    def act(self):
        dx = self.target[0] - self.assignee.float_pos[0]
        dy = self.target[1] - self.assignee.float_pos[1]
        new = atan2(dy, dx)
        self.assignee.direction = new
        if dx + dy < self.assignee.speed:
            # move to exact pos

            return True
        return False
        

TASK_NOT_STARTED = TaskStep("Task not started", [])
FARM = TaskStep("Do farming", [])
GO_HOME = TaskStep("Go home", [])
WANDER = TaskStep("Wandering")
TASK_COMPLETED = TaskStep("Task completed", [])