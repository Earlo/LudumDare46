from math import sin, cos, pi
from random import random

from engine.graphics.entity import Entity

from ..unit_logic.tasks import MoveTo


class Unit(Entity):
    idleframes = ["olive0"]
    walkingframes = ["oliveSide0", "oliveSide1", "oliveSide2"]
    walkFwdFrames = ["oliveFwd0", "oliveFwd1", "oliveFwd2"]
    walkBackFrames = ["oliveBack0", "oliveBack1", "oliveBack2"]

    direction = 0

    def __init__(self, GAME, pos):
        super().__init__(pos)
        self.speed = 0.2
        self.animationSpeed = 10.0
        self.task = None
        self.taskManager = GAME.taskManager

    def tick(self, t):
        if self.task:
            if self.task.act():
                if self.taskManager.add_to_pool(self):
                    print("No task to act on")
                    self.task = None
        else:
            target = (
                self.float_pos[0] + random() * 1000 - random() * 100,
                self.float_pos[1] + random() * 1000 - random() * 100,
            )
            self.task = MoveTo(target, self)
        super().tick(t)

    def assign(self, task, complete_task):
        self.task = task
        self.complete_task = complete_task

    @property
    def frames(self):
        if -pi / 4 <= self.direction < pi / 4:
            return self.walkingframes
        elif pi / 4 <= self.direction < 3 * pi / 4:
            return self.walkFwdFrames
        elif 3 * pi / 4 <= self.direction < 6 * pi / 4:
            return self.walkingframes
        else:
            return self.walkBackFrames

    @property
    def frameInverted(self):
        return pi / 2 >= self.direction > pi / 2

    @property
    def velocity(self):
        return (cos(self.direction) * self.speed, sin(self.direction) * self.speed)
