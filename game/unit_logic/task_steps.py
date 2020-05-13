from ..task_step import TaskStep
from ..units.plant import Plant

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


class PlantStep(TaskStep):
    def __init__(self, target, *args, **kwargs):
        title = "Planting"
        super().__init__(title)
        self.target = target

    def act(self, assignee, task):
        plant = Plant(assignee.game, self.target, 0)
        assignee.game.entities.append(plant)
        return True


class HarvestStep(TaskStep):
    def __init__(self, plant, *args, **kwargs):
        title = "Planting"
        super().__init__(title)
        self.plant = plant

    def act(self, assignee, task):
        self.plant.harvest()
        return True


class StoreStep(TaskStep):
    def __init__(self, storage, *args, **kwargs):
        title = "Storing"
        super().__init__(title)
        self.storage = storage

    def act(self, assignee, task):
        self.storage.deliver_olive()
        return True


FARM = TaskStep("Do farming", [])
GO_HOME = TaskStep("Go home", [])
WANDER = TaskStep("Wandering")
