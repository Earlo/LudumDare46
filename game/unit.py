from engine.graphics.entity import Entity


class Unit(Entity):
    sprite = ["frog"]
    graphic_layer = 1

    def __init__(self, GAME, pos, vel):
        super().__init__(pos)
        self.velocity = vel

    def tick(self, t):
        super().tick(t)
