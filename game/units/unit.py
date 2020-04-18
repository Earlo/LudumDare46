from math import sin, cos, pi
from random import random

from engine.graphics.entity import Entity

from ..unit_logic.move_to import MoveTo


class Unit(Entity):
    idleframes = ["olive0"]
    walkingframes = ["olive0", "olive1", "olive2"]
    frames = idleframes
    animationSpeed = 10.0
    graphic_layer = 1

    def __init__(self, GAME, pos):
        super().__init__(pos)
        self.direction = pi
        self.moving = False
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
            self.task = MoveTo(self, target)
        if self.moving:
            self.frames = self.walkingframes
        else:
            self.frames = self.idleframes
        super().tick(t)

    def assign(self, task, complete_task):
        self.task = task
        self.complete_task = complete_task

    @property
    def velocity(self):
        if self.moving:
            return (cos(self.direction) * self.speed, sin(self.direction) * self.speed)
        else:
            return (0, 0)
