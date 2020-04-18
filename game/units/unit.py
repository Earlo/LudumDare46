from math import sin, cos, pi
from random import random

from engine.graphics.entity import Entity

from ..unit_logic.tasks.move_to import MoveTo


class Unit(Entity):
    sprite = ["frog"]
    graphic_layer = 1

    def __init__(self, GAME, pos):
        super().__init__(pos)
        self.direction = pi
        self.speed = 0.2
        self.task = None

    def tick(self, t):
        if self.task:
            if self.task.act():
                self.task = None
        else:
            target = (
                self.float_pos[0] + random() * 100 - random() * 100,
                self.float_pos[1] + random() * 100 - random() * 100,
            )
            print(target)
            self.task = MoveTo(self, target)
            # when idle, select a nearby and wander there
            pass
        super().tick(t)

    def assign(self, task, complete_task):
        self.task = task
        self.complete_task = complete_task

    @property
    def velocity(self):
        return (cos(self.direction) * self.speed, sin(self.direction) * self.speed)
