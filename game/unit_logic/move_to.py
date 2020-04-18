from math import atan


# Todo some task superclass?
class MoveTo:
    def __init__(self, entity, target):
        self.entity = entity
        self.target = target

    def act(self):
        print(self.entity.float_pos[0])
        dx = self.entity.float_pos[0] - self.target[0]
        dy = self.entity.float_pos[1] - self.target[1]
        self.entity.direction = atan(dy / dx)
        # TODO add check if completed
