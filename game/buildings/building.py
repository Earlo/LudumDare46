from engine.graphics.entity import Entity

class Building(Entity):
    sprite = ["frog"]
    graphic_layer = 1

    def __init__(self, GAME, pos):
        super().__init__(pos)
        self.velocity = (0.0, 0.0)
        self.game = GAME

    @property
    def location(self):
        return self.pos