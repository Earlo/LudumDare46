from math import sin, cos, pi
from random import random

from engine.graphics.entity import Entity

from ..unit_logic.tasks import MoveTo


class Unit(Entity):
    idleframes = ["olive0"]
    walkingframes = ["oliveSide0", "oliveSide1", "oliveSide2"]
    walkFwdFrames = ["oliveFwd0", "oliveFwd1", "oliveFwd2"]
    walkBackFrames = ["oliveBack0", "oliveBack1", "oliveBack2"]

    def __init__(self, GAME, pos):
        super().__init__(pos)
        self.speed = 0.2
        self.animationSpeed = 10.0
        self.task = MoveTo((0, 0), self)
        self.taskManager = GAME.taskManager

    def tick(self, t):
        if self.task:
            if self.task.act():
                print("DONE!")
                completed_task = self.task
                self.task = None
                self.taskManager.get_task(self, completed_task)
        else:
            self.direction += 0.05
            self.taskManager.get_task(self)
        super().tick(t)

    @property
    def frames(self):
        if 0 <= self.direction < 1 * pi / 4:
            return self.walkingframes
        elif 1 * pi / 4 <= self.direction < 3 * pi / 4:
            return self.walkFwdFrames
        elif 3 * pi / 4 <= self.direction < 5 * pi / 4:
            return self.walkingframes
        elif 5 * pi / 4 <= self.direction < 7 * pi / 4:
            return self.walkBackFrames
        else:
            return self.walkingframes

    @property
    def frameInverted(self):
        return not (self.direction < 1 / 4 * pi or self.direction > 7 / 4 * pi)

    @property
    def velocity(self):
        return (cos(self.direction) * self.speed, sin(self.direction) * self.speed)
