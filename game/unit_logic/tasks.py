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


class HarvestOlives(Task):
    def __init__(self, plant, assignee=None):
        title = "Harvest olives at " + str(plant.topleft)
        steps = [
            task_steps.MoveTo(plant.topleft),
            task_steps.HarvestStep(plant)
            ]
        super().__init__(title, steps, assignee)


class StoreOlives(Task):
    def __init__(self, storage, assignee=None):
        title = "Store olives at " + str(storage.topleft)
        steps = [
            task_steps.MoveTo(storage.topleft),
            task_steps.StoreStep(storage)
            ]
        super().__init__(title, steps, assignee)

class HarvesAndStore(Task):
    def __init__(self, plant, storage, assignee=None):
        title = "Harvest and store olives"
        steps = [
            task_steps.MoveTo(plant.topleft),
            task_steps.HarvestStep(plant),
            task_steps.MoveTo(storage.topleft),
            task_steps.StoreStep(storage)
            ]
        super().__init__(title, steps, assignee)
