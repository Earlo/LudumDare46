from math import atan2, sqrt


# Todo some task superclass?
class MoveTo:
    def __init__(self, entity, target):
        self.entity = entity
        self.target = target

    def act(self):

        dx = self.target[0] - self.entity.float_pos[0]
        dy = self.target[1] - self.entity.float_pos[1]
        new = atan2(dy, dx)
        self.entity.direction = new
        if dx + dy < self.entity.speed:
            # move to exact pos

            return True
        return False
