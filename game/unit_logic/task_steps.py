from ..task_step import TaskStep

from math import atan2, sqrt


class MoveTo(TaskStep):
    def __init__(self, target, *args, **kwargs):
        title = "Moving to " + str(target)
        super().__init__(title)
        self.target = target

    def act(self, assignee, task):
        dx = self.target[0] - assignee.float_pos[0]
        dy = self.target[1] - assignee.float_pos[1]
        new = atan2(dy, dx)
        assignee.direction = new
        ## Todo figure proper treshold here
        if sqrt(dx ** 2 + dy ** 2) < assignee.speed * 20:
            # move to exact pos
            return True
        return False


FARM = TaskStep("Do farming", [])
GO_HOME = TaskStep("Go home", [])
WANDER = TaskStep("Wandering")
